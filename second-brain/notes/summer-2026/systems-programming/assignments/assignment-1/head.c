/*
 * Name: Srinarayan Srikanth
 * head.c - a simple implementation of the Unix head command
 *
 * Synopsis:
 *     head [-n] [file]
 *
 * Prints the first n lines of the given file to standard output. If -n is not given, n
 * defaults to 10.
 * 
 */

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int n = 10;
    FILE *fp = stdin;
    int argIndex = 1;

    /* Check for optional -n argument, e.g. -20 */
    if (argIndex < argc && argv[argIndex][0] == '-') {
        n = atoi(&argv[argIndex][1]);
        argIndex++;
    }

    /* Check for optional file name argument */
    if (argIndex < argc) {
        fp = fopen(argv[argIndex], "r");
        if (fp == NULL) {
            fprintf(stderr, "head: cannot open file '%s'\n", argv[argIndex]);
            return 1;
        }
        argIndex++;
    }

    int c;
    int lines = 0;

    while (lines < n && (c = getc(fp)) != EOF) {
        putc(c, stdout);
        if (c == '\n') {
            lines++;
        }
    }

    if (fp != stdin) {
        fclose(fp);
    }

    return 0;
}
