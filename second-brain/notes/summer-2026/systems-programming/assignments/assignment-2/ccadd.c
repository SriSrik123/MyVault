#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/file.h>
#include <sys/stat.h>
#include <unistd.h>
#include "cc.h"

int
main(int argc, char *argv[]) {
	CComp newcomp;
	FILE *fp;
	struct stat st;
	int aflag;

	if(argc != 8) {
		fprintf(stderr,
			"Usage: %s id|-a name year maker cpu memory desc\n",
			argv[0]);
		exit(1);
	}
	aflag = strcmp(argv[1], "-a") == 0;
	if(!aflag) {
		newcomp.id = atoi(argv[1]);
	}
	strncpy(newcomp.name, argv[2], 15);
	newcomp.name[15] = 0;
	newcomp.year = atoi(argv[3]);
	strncpy(newcomp.maker, argv[4], 15);
	newcomp.maker[15] = 0;
	strncpy(newcomp.cpu, argv[5], 7);
	newcomp.cpu[7] = 0;
	newcomp.memory = atoi(argv[6]);
	strncpy(newcomp.desc, argv[7], Descsz - 1);
	newcomp.desc[Descsz - 1] = 0;

	fp = fopen("ccdb", "r+");
	if(fp == NULL) {
		fp = fopen("ccdb", "w");
		if(fp == NULL) {
			perror("ccdb");
			exit(2);
		}
	}
	flock(fileno(fp), LOCK_EX);
	if(aflag) {
		fstat(fileno(fp), &st);
		newcomp.id = st.st_size / sizeof(CComp);
		if(newcomp.id == 0) {
			newcomp.id = 1;
		}
		printf("Added item %d\n", newcomp.id);
	}
	fseek(fp, newcomp.id * sizeof(CComp), SEEK_SET);
	fwrite(&newcomp, 256, 1, fp);
	flock(fileno(fp), LOCK_UN);
	fclose(fp);
}