#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#define SERVER_HOST "tux5"
#define SERVER_PORT 2026
#define BUF_SIZE 1024
static int sockfd;
void *sender_thread(void *arg) {
    char buf[BUF_SIZE];
    int n;
    while (fgets(buf, BUF_SIZE, stdin) != NULL) {
        n = strlen(buf);
        if (n <= 0) {
            continue;
        }
        if (send(sockfd, buf, n, 0) < 0) {
            perror("send");
            break;
        }
    }
    return NULL;
}
void *receiver_thread(void *arg) {
    char buf[BUF_SIZE];
    int n;
    for (;;) {
        n = recv(sockfd, buf, BUF_SIZE - 1, 0);
        if (n < 0) {
            perror("recv");
            break;
        }
        if (n == 0) {
            printf("Server closed the connection.\n");
            break;
        }
        buf[n] = '\0';
        printf("%s\n", buf);
        fflush(stdout);
    }
    exit(0);
    return NULL;
}
int main(int argc, char *argv[]) {
    struct sockaddr_in server_addr;
    struct sockaddr_in local_addr;
    struct hostent *hostinfo;
    pthread_t sender, receiver;
    char *name;
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <name>\n", argv[0]);
        exit(1);
    }
    name = argv[1];
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        perror("socket");
        exit(1);
    }
    memset(&local_addr, 0, sizeof(struct sockaddr_in));
    local_addr.sin_family = AF_INET;
    local_addr.sin_port = htons(0);
    local_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    if (bind(sockfd, (struct sockaddr *)&local_addr,
             sizeof(struct sockaddr_in)) < 0) {
        perror("bind");
        exit(1);
    }
    hostinfo = gethostbyname(SERVER_HOST);
    if (hostinfo == NULL) {
        fprintf(stderr, "Could not resolve host %s\n", SERVER_HOST);
        exit(1);
    }
    memset(&server_addr, 0, sizeof(struct sockaddr_in));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(SERVER_PORT);
    memcpy(&server_addr.sin_addr, hostinfo->h_addr_list[0], hostinfo->h_length);
    if (connect(sockfd, (struct sockaddr *)&server_addr,
                sizeof(struct sockaddr_in)) < 0) {
        perror("connect");
        exit(1);
    }
    if (send(sockfd, name, strlen(name), 0) < 0) {
        perror("send (name)");
        exit(1);
    }
    if (pthread_create(&sender, NULL, sender_thread, NULL) != 0) {
        perror("pthread_create sender");
        exit(1);
    }
    if (pthread_create(&receiver, NULL, receiver_thread, NULL) != 0) {
        perror("pthread_create receiver");
        exit(1);
    }
    pthread_join(sender, NULL);
    pthread_join(receiver, NULL);
    shutdown(sockfd, SHUT_RDWR);
    close(sockfd);
    return 0;
}
