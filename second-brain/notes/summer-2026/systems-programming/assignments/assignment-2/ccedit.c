#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/file.h>
#include "cc.h"

int
main(int argc, char *argv[]) {
	int id;
	FILE *fp;
	CComp comp;
	char line[256];

	if(argc != 2) {
		fprintf(stderr, "Usage: %s ID\n", argv[0]);
		exit(1);
	}
	id = atoi(argv[1]);
	fp = fopen("ccdb", "r+");
	if(fp == NULL) {
		fprintf(stderr, "No DB\n");
		exit(2);
	}
	flock(fileno(fp), LOCK_EX);
	fseek(fp, id * sizeof(CComp), SEEK_SET);
	if(fread(&comp, sizeof(CComp), 1, fp) != 1 || comp.id == 0) {
		fprintf(stderr, "Item not found\n");
		flock(fileno(fp), LOCK_UN);
		fclose(fp);
		exit(3);
	}

	printf("Name [%s]: ", comp.name);
	fflush(stdout);
	if(fgets(line, sizeof(line), stdin) != NULL) {
		line[strcspn(line, "\n")] = 0;
		if(line[0] != 0) {
			strncpy(comp.name, line, 15);
			comp.name[15] = 0;
		}
	}

	printf("Year [%d]: ", comp.year);
	fflush(stdout);
	if(fgets(line, sizeof(line), stdin) != NULL) {
		line[strcspn(line, "\n")] = 0;
		if(line[0] != 0) {
			comp.year = atoi(line);
		}
	}

	printf("Maker [%s]: ", comp.maker);
	fflush(stdout);
	if(fgets(line, sizeof(line), stdin) != NULL) {
		line[strcspn(line, "\n")] = 0;
		if(line[0] != 0) {
			strncpy(comp.maker, line, 15);
			comp.maker[15] = 0;
		}
	}

	printf("CPU [%s]: ", comp.cpu);
	fflush(stdout);
	if(fgets(line, sizeof(line), stdin) != NULL) {
		line[strcspn(line, "\n")] = 0;
		if(line[0] != 0) {
			strncpy(comp.cpu, line, 7);
			comp.cpu[7] = 0;
		}
	}

	printf("Memory [%d]: ", comp.memory);
	fflush(stdout);
	if(fgets(line, sizeof(line), stdin) != NULL) {
		line[strcspn(line, "\n")] = 0;
		if(line[0] != 0) {
			comp.memory = atoi(line);
		}
	}

	printf("Description [%s]: ", comp.desc);
	fflush(stdout);
	if(fgets(line, sizeof(line), stdin) != NULL) {
		line[strcspn(line, "\n")] = 0;
		if(line[0] != 0) {
			strncpy(comp.desc, line, Descsz - 1);
			comp.desc[Descsz - 1] = 0;
		}
	}

	fseek(fp, id * sizeof(CComp), SEEK_SET);
	fwrite(&comp, sizeof(CComp), 1, fp);
	flock(fileno(fp), LOCK_UN);
	fclose(fp);
}
