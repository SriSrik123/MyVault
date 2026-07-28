#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFSIZE 256


typedef struct item{
  char *word;
  int weight;
}Item;

void mergeAlpha(Item *arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    Item *L = malloc(n1 * sizeof(Item));
    Item *R = malloc(n2 * sizeof(Item));
    for (int i = 0; i < n1; i++) L[i] = arr[left + i];
    for (int j = 0; j < n2; j++) R[j] = arr[mid + 1 + j];
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (strcmp(L[i].word, R[j].word) <= 0) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
    free(L);
    free(R);
}

void mergeSortAlpha(Item *arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSortAlpha(arr, left, mid);
        mergeSortAlpha(arr, mid + 1, right);
        mergeAlpha(arr, left, mid, right);
    }
}

void mergeWeight(Item *arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    Item *L = malloc(n1 * sizeof(Item));
    Item *R = malloc(n2 * sizeof(Item));
    for (int i = 0; i < n1; i++) L[i] = arr[left + i];
    for (int j = 0; j < n2; j++) R[j] = arr[mid + 1 + j];
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i].weight >= R[j].weight) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
    free(L);
    free(R);
}

void mergeSortWeight(Item *arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSortWeight(arr, left, mid);
        mergeSortWeight(arr, mid + 1, right);
        mergeWeight(arr, left, mid, right);
    }
}

int binarySearchLeft(Item *dict, int wordCount, const char *prefix, int prefixLen) {
    int lo = 0, hi = wordCount - 1, result = -1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        int cmp = strncmp(dict[mid].word, prefix, prefixLen);
        if (cmp == 0) { result = mid; hi = mid - 1; }
        else if (cmp < 0) lo = mid + 1;
        else hi = mid - 1;
    }
    return result;
}

int main(int argc, char **argv) {
    char *dictionaryFilePath = argv[1]; //this keeps the path to dictionary file
    char *queryFilePath = argv[2]; //this keeps the path to the file that keeps a list of query wrods, 1 query per line
    int wordCount=0; //this variable will keep a count of words in the dictionary, telling us how much memory to allocate
    int queryCount=0; //this variable will keep a count of queries in the query file, telling us how much memory to allocate for the query words

    ////////////////////////////////////////////////////////////////////////
    ///////////////////////// read dictionary file /////////////////////////
    ////////////////////////////////////////////////////////////////////////
    FILE *fp = fopen(dictionaryFilePath, "r");
    char *line = NULL; //variable to be used for line counting
    size_t lineBuffSize = 0; //variable to be used for line counting
    ssize_t lineSize; //variable to be used for line counting

    //check if the file is accessible, just to make sure...
    if(fp == NULL){
        fprintf(stderr, "Error opening file:%s\n",dictionaryFilePath);
        return -1;
    }

    //First, let's count number of lines. This will help us know how much memory to allocate
    while((lineSize = getline(&line,&lineBuffSize,fp)) !=-1)
    {
        wordCount++;
    }

    //Printing wordCount for debugging purposes. You can remove this part from your submission.
    //printf("%d\n",wordCount);

    /////////////////PAY ATTENTION HERE/////////////////
    //This might be a good place to allocate memory for your data structure, by the size of "wordCount"
    ////////////////////////////////////////////////////
    Item *dict = malloc(wordCount * sizeof(Item));

    //Read the file once more, this time to fill in the data into memory
    fseek(fp, 0, SEEK_SET);// rewind to the beginning of the file, before reading it line by line.
    char word[BUFSIZE]; //to be used for reading lines in the loop below
    int weight;
    for(int i = 0; i < wordCount; i++)
    {
        fscanf(fp, "%s %d\n",word,&weight);
        //Let's print them to the screen to make sure we can read input, for debugging purposes. You can remove this part from your submission.
        //printf("%s %d\n",word,weight);

        /////////////////PAY ATTENTION HERE/////////////////
        //This might be a good place to store the dictionary words into your data structure
        ////////////////////////////////////////////////////
        dict[i].word = strdup(word);
        dict[i].weight = weight;
    }
    //close the input file
    fclose(fp);

    mergeSortAlpha(dict, 0, wordCount - 1);

    ////////////////////////////////////////////////////////////////////////
    ///////////////////////// read query list file /////////////////////////
    ////////////////////////////////////////////////////////////////////////
    fp = fopen(queryFilePath, "r");

    //check if the file is accessible, just to make sure...
    if(fp == NULL){
        fprintf(stderr, "Error opening file:%s\n",queryFilePath);
        return -1;
    }

    //First, let's count number of queries. This will help us know how much memory to allocate
    while((lineSize = getline(&line,&lineBuffSize,fp)) !=-1)
    {
        queryCount++;
    }
    free(line); //getline internally allocates memory, so we need to free it here so as not to leak memory!!

    //Printing line count for debugging purposes. You can remove this part from your submission.
    //printf("%d\n",queryCount);

    /////////////////PAY ATTENTION HERE/////////////////
    //This might be a good place to allocate memory for storing query words, by the size of "queryCount"
    ////////////////////////////////////////////////////
    char **queries = malloc(queryCount * sizeof(char *));

    fseek(fp, 0, SEEK_SET);// rewind to the beginning of the file, before reading it line by line.
    for(int i = 0; i < queryCount; i++)
    {
        fscanf(fp, "%s\n",word);
        //Let's print them to the screen to make sure we can read input, for debugging purposes. You can remove this part from your submission.
        //printf("%s %d\n",word);

        /////////////////PAY ATTENTION HERE/////////////////
        //This might be a good place to store the query words in a list like data structure
        ////////////////////////////////////////////////////
        queries[i] = strdup(word);
    }
    //close the input file
    fclose(fp);

    ////////////////////////////////////////////////////////////////////////
    ///////////////////////// reading input is done ////////////////////////
    ////////////////////////////////////////////////////////////////////////

    //Now it is your turn to do the magic!!!
    //do search/sort/print, whatever you think you need to do to satisfy the requirements of the assignment!
    //loop through the query words and list suggestions for each query word if there are any
    //don't forget to free the memory before you quit the program!

    //OUTPUT SPECS:
    // use the following if no word to suggest: printf("No suggestion!\n");
    // use the following to print a single line of outputs (assuming that the word and weight are stored in variables named word and weight, respectively):
    // printf("%s %d\n",word,weight);
    // if there are more than 10 outputs to print, you should print the top 10 weighted outputs.

    for (int i = 0; i < queryCount; i++) {
        printf("Query word:%s\n", queries[i]);
        int prefixLen = strlen(queries[i]);
        int start = binarySearchLeft(dict, wordCount, queries[i], prefixLen);
        if (start == -1) {
            printf("No suggestion!\n");
        } else {
            int end = start;
            while (end < wordCount && strncmp(dict[end].word, queries[i], prefixLen) == 0) {
                end++;
            }
            int matchCount = end - start;
            Item *matches = malloc(matchCount * sizeof(Item));
            for (int j = 0; j < matchCount; j++) {
                matches[j] = dict[start + j];
            }
            mergeSortWeight(matches, 0, matchCount - 1);
            int printCount = matchCount < 10 ? matchCount : 10;
            for (int j = 0; j < printCount; j++) {
                printf("%s %d\n", matches[j].word, matches[j].weight);
            }
            free(matches);
        }
    }

    for (int i = 0; i < wordCount; i++) free(dict[i].word);
    free(dict);
    for (int i = 0; i < queryCount; i++) free(queries[i]);
    free(queries);

    return 0;
}
