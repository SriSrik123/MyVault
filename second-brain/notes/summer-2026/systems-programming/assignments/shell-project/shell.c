#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <fcntl.h>

#define MAX_ARGS 64
#define MAX_LINE 1024

int main() {
    char *line = NULL;
    size_t len = 0;
    ssize_t read;

    while (1) {
        printf("myshell> ");
        fflush(stdout);

        read = getline(&line, &len, stdin);
        
        if (read == -1) {
            printf("\n");
            break;
        }

        if (read > 0 && line[read - 1] == '\n') {
            line[read - 1] = '\0';
        }

        int num_commands = 0;
        char *commands[MAX_ARGS];
        char *saveptr1;
        char *cmd_token = strtok_r(line, "|", &saveptr1);
        while (cmd_token != NULL && num_commands < MAX_ARGS - 1) {
            commands[num_commands++] = cmd_token;
            cmd_token = strtok_r(NULL, "|", &saveptr1);
        }
        commands[num_commands] = NULL;

        if (num_commands == 0) {
            continue;
        }

        int pipefds[2];
        int prev_pipe_read_fd = -1;
        pid_t pids[MAX_ARGS];
        int num_pids = 0;
        int should_exit = 0;

        for (int c = 0; c < num_commands; c++) {
            int i = 0;
            char *args[MAX_ARGS];
            char *saveptr2;
            char *token = strtok_r(commands[c], " \t", &saveptr2);
            while (token != NULL && i < MAX_ARGS - 1) {
                args[i++] = token;
                token = strtok_r(NULL, " \t", &saveptr2);
            }
            args[i] = NULL;

            if (args[0] == NULL) {
                continue;
            }

            char *infile = NULL;
            char *outfile = NULL;
            int argc = 0;
            char *clean_args[MAX_ARGS];
            for (int j = 0; args[j] != NULL; j++) {
                if (strcmp(args[j], "<") == 0) {
                    if (args[j + 1] == NULL) {
                        fprintf(stderr, "myshell: expected filename after '<'\n");
                        argc = -1;
                        break;
                    }
                    infile = args[++j];
                } else if (strcmp(args[j], ">") == 0) {
                    if (args[j + 1] == NULL) {
                        fprintf(stderr, "myshell: expected filename after '>'\n");
                        argc = -1;
                        break;
                    }
                    outfile = args[++j];
                } else {
                    clean_args[argc++] = args[j];
                }
            }
            clean_args[argc] = NULL;

            if (argc <= 0) {
                continue;
            }

            if (num_commands == 1 && strcmp(clean_args[0], "cd") == 0) {
                if (clean_args[1] == NULL) {
                    char *home = getenv("HOME");
                    if (home != NULL) {
                        if (chdir(home) != 0) {
                            perror("cd");
                        }
                    } else {
                        fprintf(stderr, "cd: HOME not set\n");
                    }
                } else {
                    if (chdir(clean_args[1]) != 0) {
                        perror("cd");
                    }
                }
                break;
            }

            if (num_commands == 1 && strcmp(clean_args[0], "exit") == 0) {
                should_exit = 1;
                break;
            }

            if (c < num_commands - 1) {
                if (pipe(pipefds) == -1) {
                    perror("pipe");
                    break;
                }
            }

            pid_t pid = fork();
            if (pid < 0) {
                perror("fork");
                break;
            } else if (pid == 0) {
                if (prev_pipe_read_fd != -1) {
                    dup2(prev_pipe_read_fd, STDIN_FILENO);
                    close(prev_pipe_read_fd);
                }
                if (c < num_commands - 1) {
                    dup2(pipefds[1], STDOUT_FILENO);
                    close(pipefds[0]);
                    close(pipefds[1]);
                }
                if (infile != NULL) {
                    int fd = open(infile, O_RDONLY);
                    if (fd < 0) {
                        perror(infile);
                        exit(EXIT_FAILURE);
                    }
                    dup2(fd, STDIN_FILENO);
                    close(fd);
                }
                if (outfile != NULL) {
                    int fd = open(outfile, O_WRONLY | O_CREAT | O_TRUNC, 0644);
                    if (fd < 0) {
                        perror(outfile);
                        exit(EXIT_FAILURE);
                    }
                    dup2(fd, STDOUT_FILENO);
                    close(fd);
                }
                if (execvp(clean_args[0], clean_args) == -1) {
                    perror(clean_args[0]);
                }
                exit(EXIT_FAILURE);
            } else {
                pids[num_pids++] = pid;
                if (prev_pipe_read_fd != -1) {
                    close(prev_pipe_read_fd);
                }
                if (c < num_commands - 1) {
                    prev_pipe_read_fd = pipefds[0];
                    close(pipefds[1]);
                }
            }
        }

        for (int c = 0; c < num_pids; c++) {
            int status;
            waitpid(pids[c], &status, WUNTRACED);
        }

        if (should_exit) {
            break;
        }
    }

    free(line);
    return 0;
}
