#include <stdio.h>
#include <stdlib.h>
#include <sys/file.h>
#include "cc.h"

int
main(int argc, char *argv[]) {
	FILE *fp;
	CComp comp;
	int y1, y2, lo, hi;

	if(argc != 3) {
		fprintf(stderr, "Usage: %s year1 year2\n", argv[0]);
		exit(1);
	}
	y1 = atoi(argv[1]);
	y2 = atoi(argv[2]);
	lo = y1 < y2 ? y1 : y2;
	hi = y1 < y2 ? y2 : y1;
	fp = fopen("ccdb", "r");
	if(fp == NULL) {
		fprintf(stderr, "No DB\n");
		exit(2);
	}
	flock(fileno(fp), LOCK_SH);
	fseek(fp, sizeof(CComp), SEEK_SET);
	while(1) {
		if(fread(&comp, sizeof(CComp), 1, fp) != 1) {
			break;
		}
		if(comp.id == 0) {
			continue;
		}
		if(comp.year < lo || comp.year > hi) {
			continue;
		}
		printf("ID: %d\n", comp.id);
		printf("Name: %s\n", comp.name);
		printf("Year: %d\n", comp.year);
		printf("Maker: %s\n", comp.maker);
		printf("CPU: %s\n", comp.cpu);
		printf("Memory: %d\n", comp.memory);
		printf("Description: %s\n", comp.desc);
		putchar('\n');
	}
	flock(fileno(fp), LOCK_UN);
	fclose(fp);
}
