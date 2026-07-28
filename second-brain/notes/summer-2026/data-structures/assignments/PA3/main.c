#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFSIZE 256
#define TABLE_SIZE 200003



typedef struct Node {
    char *word;
    struct Node *next;
} Node;

Node *hashTable[TABLE_SIZE];

unsigned int hash(const char *str) {
    unsigned int h = 0;
    while (*str) {
        h = h * 31 + (unsigned char)(*str);
        str++;
    }
    return h % TABLE_SIZE;
}

void insert(const char *word) {
    unsigned int idx = hash(word);
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->word = (char *)malloc(strlen(word) + 1);
    strcpy(newNode->word, word);
    newNode->next = hashTable[idx];
    hashTable[idx] = newNode;
}

int search(const char *word) {
    unsigned int idx = hash(word);
    Node *curr = hashTable[idx];
    while (curr != NULL) {
        if (strcmp(curr->word, word) == 0)
            return 1;
        curr = curr->next;
    }
    return 0;
}

char suggestions[200][BUFSIZE];
int suggCount;

void addSuggestion(const char *word) {
    for (int i = 0; i < suggCount; i++) {
        if (strcmp(suggestions[i], word) == 0)
            return;
    }
    strcpy(suggestions[suggCount++], word);
}

void findSuggestions(const char *word) {
    suggCount = 0;
    int len = strlen(word);
    char temp[BUFSIZE];

    /* 1. Inverted adjacent letters */
    strcpy(temp, word);
    for (int i = 0; i < len - 1; i++) {
        char t = temp[i];
        temp[i] = temp[i + 1];
        temp[i + 1] = t;
        if (search(temp))
            addSuggestion(temp);
        t = temp[i];
        temp[i] = temp[i + 1];
        temp[i + 1] = t;
    }

    /* 2. Missing letter at the beginning (insert each letter before the word) */
    for (char c = 'a'; c <= 'z'; c++) {
        temp[0] = c;
        strcpy(temp + 1, word);
        if (search(temp))
            addSuggestion(temp);
    }

    /* 3. Missing letter at the end (append each letter after the word) */
    strcpy(temp, word);
    for (char c = 'a'; c <= 'z'; c++) {
        temp[len] = c;
        temp[len + 1] = '\0';
        if (search(temp))
            addSuggestion(temp);
    }

    /* 4. Extra letter at the beginning (remove first character) */
    if (len > 1) {
        strcpy(temp, word + 1);
        if (search(temp))
            addSuggestion(temp);
    }

    /* 5. Extra letter at the end (remove last character) */
    if (len > 1) {
        strncpy(temp, word, len - 1);
        temp[len - 1] = '\0';
        if (search(temp))
            addSuggestion(temp);
    }
}

int main(int argc, char **argv)
{
    char *dictionaryFilePath = argv[1];
    char *inputFilePath = argv[2];
    char *check = argv[3];
    int numOfWords = 0;

    int insertToDictionary;
    if (strcmp(check, "add") == 0)
        insertToDictionary = 1;
    else
        insertToDictionary = 0;

    /* Initialize hash table */
    for (int i = 0; i < TABLE_SIZE; i++)
        hashTable[i] = NULL;

    ////////////////////////////////////////////////////////////////////
    // read dictionary file
    FILE *fp = fopen(dictionaryFilePath, "r");
    char *line = NULL;
    size_t lineBuffSize = 0;
    ssize_t lineSize;

    if (fp == NULL) {
        fprintf(stderr, "Error opening file\n");
        exit(1);
    }

    while ((lineSize = getline(&line, &lineBuffSize, fp)) != -1)
        numOfWords++;
    free(line);
    line = NULL;
    lineBuffSize = 0;

    fseek(fp, 0, SEEK_SET);

    char wrd[BUFSIZE];
    for (int i = 0; i < numOfWords; i++) {
        fscanf(fp, "%s \n", wrd);
        insert(wrd);
    }
    fclose(fp);

    ////////////////////////////////////////////////////////////////////
    // read the input text file word by word
    fp = fopen(inputFilePath, "r");

    if (fp == NULL) {
        fprintf(stderr, "Error opening file\n");
        return -1;
    }

    int noTypo = 1;

    while ((lineSize = getline(&line, &lineBuffSize, fp)) != -1) {
        char *word;
        const char delimiter[] = " ,.:;!\n";
        word = strtok(line, delimiter);

        while (word != NULL) {
            if (!search(word)) {
                noTypo = 0;
                printf("Misspelled word: %s\n", word);

                findSuggestions(word);
                printf("Suggestions:");
                for (int i = 0; i < suggCount; i++)
                    printf(" %s", suggestions[i]);
                printf("\n");

                if (insertToDictionary)
                    insert(word);
            }
            word = strtok(NULL, delimiter);
        }
    }
    free(line);
    fclose(fp);

    if (noTypo == 1)
        printf("No typo!\n");

    /* Free hash table memory */
    for (int i = 0; i < TABLE_SIZE; i++) {
        Node *curr = hashTable[i];
        while (curr != NULL) {
            Node *next = curr->next;
            free(curr->word);
            free(curr);
            curr = next;
        }
    }

    return 0;
}
