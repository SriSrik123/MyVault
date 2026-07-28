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
	memset(&comp, 0, sizeof(CComp));
	fseek(fp, id * sizeof(CComp), SEEK_SET);
	fwrite(&comp, sizeof(CComp), 1, fp);
	flock(fileno(fp), LOCK_UN);
	fclose(fp);
}
