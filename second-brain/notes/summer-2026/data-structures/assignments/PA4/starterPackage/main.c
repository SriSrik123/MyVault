#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/* ─────────────────────────────────────────────
   Data Structures
   ───────────────────────────────────────────── */

/* Binary tree node for the Huffman tree */
typedef struct TreeNode {
    unsigned char ch;          /* character (only meaningful at leaf) */
    unsigned int  freq;
    struct TreeNode *left, *right;
} TreeNode;


/* Min-heap (priority queue) of TreeNode pointers */
typedef struct {
    TreeNode **arr;
    int size;
    int capacity;
} MinHeap;

/* Code table entry – one slot per possible ASCII value (0-255) */
typedef struct {
    unsigned int freq;
    char *binary_code;
} Code;

/* ─────────────────────────────────────────────
   Tree helpers
   ───────────────────────────────────────────── */

static TreeNode *newNode(unsigned char ch, unsigned int freq) {
    TreeNode *n = malloc(sizeof(TreeNode));
    n->ch    = ch;
    n->freq  = freq;
    n->left  = n->right = NULL;
    return n;
}

static void freeTree(TreeNode *node) {
    if (!node) return;
    freeTree(node->left);
    freeTree(node->right);
    free(node);
}

/* ─────────────────────────────────────────────
   Min-Heap helpers
   ───────────────────────────────────────────── */

static MinHeap *createHeap(int capacity) {
    MinHeap *h = malloc(sizeof(MinHeap));
    h->arr      = malloc(sizeof(TreeNode *) * capacity);
    h->size     = 0;
    h->capacity = capacity;
    return h;
}

static void swapNodes(TreeNode **a, TreeNode **b) {
    TreeNode *tmp = *a; *a = *b; *b = tmp;
}

static void heapifyDown(MinHeap *h, int i) {
    int smallest = i;
    int l = 2*i + 1, r = 2*i + 2;
    if (l < h->size && h->arr[l]->freq < h->arr[smallest]->freq) smallest = l;
    if (r < h->size && h->arr[r]->freq < h->arr[smallest]->freq) smallest = r;
    if (smallest != i) {
        swapNodes(&h->arr[i], &h->arr[smallest]);
        heapifyDown(h, smallest);
    }
}

static void heapifyUp(MinHeap *h, int i) {
    int parent = (i - 1) / 2;
    if (i > 0 && h->arr[i]->freq < h->arr[parent]->freq) {
        swapNodes(&h->arr[i], &h->arr[parent]);
        heapifyUp(h, parent);
    }
}

static void insertHeap(MinHeap *h, TreeNode *node) {
    h->arr[h->size++] = node;
    heapifyUp(h, h->size - 1);
}

static TreeNode *extractMin(MinHeap *h) {
    TreeNode *min   = h->arr[0];
    h->arr[0]       = h->arr[--h->size];
    heapifyDown(h, 0);
    return min;
}

/* ─────────────────────────────────────────────
   Huffman Tree Construction
   ───────────────────────────────────────────── */

static TreeNode *buildHuffmanTree(Code *codeTable) {
    /* Count unique characters */
    int uniqueCount = 0;
    for (int i = 0; i < 256; i++)
        if (codeTable[i].freq > 0) uniqueCount++;

    if (uniqueCount == 0) return NULL;

    MinHeap *heap = createHeap(uniqueCount * 2 + 2);

    for (int i = 0; i < 256; i++)
        if (codeTable[i].freq > 0)
            insertHeap(heap, newNode((unsigned char)i, codeTable[i].freq));

    /* Merge the two smallest until one node remains */
    while (heap->size > 1) {
        TreeNode *left  = extractMin(heap);
        TreeNode *right = extractMin(heap);
        TreeNode *parent = newNode(0, left->freq + right->freq);
        parent->left  = left;
        parent->right = right;
        insertHeap(heap, parent);
    }

    TreeNode *root = extractMin(heap);
    free(heap->arr);
    free(heap);
    return root;
}

/* ─────────────────────────────────────────────
   Code Assignment (DFS)
   ───────────────────────────────────────────── */

static void assignCodes(TreeNode *node, char *buf, int depth, Code *codeTable) {
    if (!node) return;

    if (!node->left && !node->right) {
        /* Leaf: record the code accumulated so far */
        buf[depth] = '\0';
        codeTable[node->ch].binary_code = malloc(depth + 1);
        strcpy(codeTable[node->ch].binary_code, buf);
        return;
    }

    buf[depth] = '0';
    assignCodes(node->left,  buf, depth + 1, codeTable);
    buf[depth] = '1';
    assignCodes(node->right, buf, depth + 1, codeTable);
}

/* ─────────────────────────────────────────────
   ENCODER
   ───────────────────────────────────────────── */

static void encode(const char *inputPath, const char *codeTablePath,
                   const char *encodedPath)
{
    /* ── 1. Count character frequencies ── */
    FILE *fin = fopen(inputPath, "r");
    if (!fin) { printf("Could not open file to read: %s\n", inputPath); return; }

    Code *codeTable = malloc(sizeof(Code) * 256);
    for (int i = 0; i < 256; i++) {
        codeTable[i].freq        = 0;
        codeTable[i].binary_code = NULL;
    }

    int c, totalChars = 0;
    while ((c = fgetc(fin)) != EOF && c != '\n') {
        codeTable[(unsigned char)c].freq++;
        totalChars++;
    }
    fclose(fin);

    /* ── 2. Build Huffman tree and assign codes ── */
    TreeNode *root = buildHuffmanTree(codeTable);

    if (root) {
        if (!root->left && !root->right) {
            /* Only one unique character: assign code "0" */
            codeTable[root->ch].binary_code = malloc(2);
            strcpy(codeTable[root->ch].binary_code, "0");
        } else {
            char buf[256];
            assignCodes(root, buf, 0, codeTable);
        }
        freeTree(root);
    }

    /* ── 3. Collect characters, sort by freq ── */
    int chars[256];
    int numUnique = 0;
    for (int i = 0; i < 256; i++)
        if (codeTable[i].freq > 0) chars[numUnique++] = i;

    /* Insertion sort descending by frequency */
    for (int i = 1; i < numUnique; i++) {
        int key = chars[i], j = i - 1;
        while (j >= 0 && codeTable[chars[j]].freq < codeTable[key].freq) {
            chars[j+1] = chars[j];
            j--;
        }
        chars[j+1] = key;
    }

    /* ── 4. Write code table ── */
    FILE *fct = fopen(codeTablePath, "w");
    if (!fct) { printf("Could not open file to write: %s\n", codeTablePath); return; }

    for (int i = 0; i < numUnique; i++) {
        int idx = chars[i];
        fprintf(fct, "%c\t%s\t%d\n",
                (unsigned char)idx,
                codeTable[idx].binary_code,
                codeTable[idx].freq);
    }
    fclose(fct);

    /* ── 5. Encode text and write encoded file ── */
    FILE *fin2 = fopen(inputPath, "r");
    FILE *fenc = fopen(encodedPath, "w");
    if (!fin2 || !fenc) { printf("Could not open files for encoding\n"); return; }

    int compressedBits = 0;
    while ((c = fgetc(fin2)) != EOF && c != '\n') {
        unsigned char uc = (unsigned char)c;
        fprintf(fenc, "%s", codeTable[uc].binary_code);
        compressedBits += (int)strlen(codeTable[uc].binary_code);
    }
    fclose(fin2);
    fclose(fenc);

    /* ── 6. Print compression statistics ── */
    printf("Original: %d bits\n",    totalChars * 8);
    printf("Compressed: %d bits\n",  compressedBits);
    printf("Compression Ratio: %.2f%%\n",
           (float)compressedBits / ((float)totalChars * 8) * 100.0f);

    /* ── 7. Clean up ── */
    for (int i = 0; i < 256; i++)
        if (codeTable[i].binary_code) free(codeTable[i].binary_code);
    free(codeTable);
}

/* ─────────────────────────────────────────────
   DECODER
   ───────────────────────────────────────────── */

/* Insert a character into the trie being used as the Huffman tree */
static void insertCode(TreeNode *root, const char *code, unsigned char ch) {
    TreeNode *cur = root;
    for (int i = 0; code[i] != '\0'; i++) {
        if (code[i] == '0') {
            if (!cur->left)  cur->left  = newNode(0, 0);
            cur = cur->left;
        } else {
            if (!cur->right) cur->right = newNode(0, 0);
            cur = cur->right;
        }
    }
    cur->ch = ch;
}

static void decode(const char *codeTablePath, const char *encodedPath,
                   const char *decodedPath)
{
    /* ── 1. Read code table and reconstruct the Huffman trie ── */
    FILE *fct = fopen(codeTablePath, "r");
    if (!fct) { printf("Could not open file to read: %s\n", codeTablePath); return; }

    TreeNode *root = newNode(0, 0);
    char line[512];

    while (fgets(line, sizeof(line), fct)) {
        /* Format: char \t code \t freq \n */
        if (line[0] == '\0' || line[0] == '\n') continue;

        unsigned char ch = (unsigned char)line[0];

        /* Skip the tab after the character */
        char *ptr = line + 1;
        if (*ptr != '\t') continue;
        ptr++;

        /* Read the binary code string */
        char code[256];
        int ci = 0;
        while (*ptr == '0' || *ptr == '1')
            code[ci++] = *ptr++;
        code[ci] = '\0';

        insertCode(root, code, ch);
    }
    fclose(fct);

    /* ── 2. Read encoded bits and traverse trie to decode ── */
    FILE *fenc = fopen(encodedPath, "r");
    FILE *fdec = fopen(decodedPath, "w");
    if (!fenc || !fdec) { printf("Could not open files for decoding\n"); return; }

    TreeNode *cur = root;
    int bit;
    while ((bit = fgetc(fenc)) != EOF && bit != '\n') {
        cur = (bit == '0') ? cur->left : cur->right;
        if (!cur) break; /* malformed input */

        if (!cur->left && !cur->right) {
            /* Reached a leaf: emit the character */
            fprintf(fdec, "%c", cur->ch);
            cur = root;
        }
    }
    fclose(fenc);
    fclose(fdec);

    freeTree(root);
}

/* ─────────────────────────────────────────────
   MAIN
   ───────────────────────────────────────────── */

int main(int argc, char **argv) {
    if (argc != 5) {
        printf("Usage:\n");
        printf("  %s encode plainText.txt codeTable.txt encodedText.txt\n", argv[0]);
        printf("  %s decode codeTable.txt encodedText.txt decodedText.txt\n", argv[0]);
        return 1;
    }

    if (strcmp(argv[1], "encode") == 0) {
        encode(argv[2], argv[3], argv[4]);
    } else if (strcmp(argv[1], "decode") == 0) {
        decode(argv[2], argv[3], argv[4]);
    } else {
        printf("Unknown mode: %s (expected 'encode' or 'decode')\n", argv[1]);
        return 1;
    }

    return 0;
}
