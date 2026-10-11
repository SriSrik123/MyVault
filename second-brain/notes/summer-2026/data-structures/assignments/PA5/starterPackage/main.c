#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int k;
static int N;

typedef struct {
    long parent;
    unsigned char tile;
    unsigned char blank;
} Node;

static unsigned char *boards = NULL;
static Node *nodes = NULL;
static long nodeCount = 0;
static long nodeCap = 0;

static long *table = NULL;
static long tableSize = 0;
static long tableMask = 0;
static long tableUsed = 0;

static void die(const char *msg)
{
    fprintf(stderr, "%s\n", msg);
    exit(EXIT_FAILURE);
}

static unsigned long hashBoard(const unsigned char *b)
{
    unsigned long h = 1469598103934665603UL;
    for (int i = 0; i < N; i++) {
        h ^= (unsigned long)b[i];
        h *= 1099511628211UL;
    }
    return h;
}

static void tableGrow(void)
{
    long newSize = tableSize * 2;
    long newMask = newSize - 1;
    long *fresh = malloc((size_t)newSize * sizeof(long));
    if (fresh == NULL)
        die("Out of memory growing the visited table.");

    for (long i = 0; i < newSize; i++)
        fresh[i] = -1;

    for (long i = 0; i < tableSize; i++) {
        if (table[i] == -1)
            continue;
        unsigned long h = hashBoard(boards + (size_t)table[i] * N);
        long pos = (long)(h & (unsigned long)newMask);
        while (fresh[pos] != -1)
            pos = (pos + 1) & newMask;
        fresh[pos] = table[i];
    }

    free(table);
    table = fresh;
    tableSize = newSize;
    tableMask = newMask;
}

static int tableSeenOrInsert(const unsigned char *b, long idx)
{
    unsigned long h = hashBoard(b);
    long pos = (long)(h & (unsigned long)tableMask);

    while (table[pos] != -1) {
        if (memcmp(boards + (size_t)table[pos] * N, b, (size_t)N) == 0)
            return 1;
        pos = (pos + 1) & tableMask;
    }

    table[pos] = idx;
    tableUsed++;
    if (tableUsed * 3 > tableSize * 2)
        tableGrow();
    return 0;
}

static void reserveNode(void)
{
    if (nodeCount < nodeCap)
        return;

    nodeCap = nodeCap ? nodeCap * 2 : 4096;
    Node *n = realloc(nodes, (size_t)nodeCap * sizeof(Node));
    unsigned char *b = realloc(boards, (size_t)nodeCap * (size_t)N);
    if (n == NULL || b == NULL)
        die("Out of memory storing search nodes.");
    nodes = n;
    boards = b;
}

static int isSolvable(const unsigned char *b)
{
    long inversions = 0;
    int blankRow = 0;

    for (int i = 0; i < N; i++) {
        if (b[i] == 0) {
            blankRow = i / k;
            continue;
        }
        for (int j = i + 1; j < N; j++)
            if (b[j] != 0 && b[j] < b[i])
                inversions++;
    }

    if (k % 2 == 1)
        return inversions % 2 == 0;
    return (inversions + blankRow) % 2 == 1;
}

int main(int argc, char **argv)
{
    if (argc < 3) {
        printf("Usage: %s <input file> <output file>\n", argv[0]);
        return -1;
    }

    FILE *fp_in = fopen(argv[1], "r");
    if (fp_in == NULL) {
        printf("Could not open a file.\n");
        return -1;
    }

    FILE *fp_out = fopen(argv[2], "w");
    if (fp_out == NULL) {
        printf("Could not open a file.\n");
        fclose(fp_in);
        return -1;
    }

    char *line = NULL;
    size_t lineBuffSize = 0;

    if (getline(&line, &lineBuffSize, fp_in) == -1)
        die("Malformed input file.");
    if (fscanf(fp_in, "%d\n", &k) != 1)
        die("Malformed input file.");
    if (getline(&line, &lineBuffSize, fp_in) == -1)
        die("Malformed input file.");

    N = k * k;

    unsigned char *start = malloc((size_t)N);
    unsigned char *goal = malloc((size_t)N);
    if (start == NULL || goal == NULL)
        die("Out of memory reading the board.");

    int blankPos = 0;
    for (int i = 0; i < N; i++) {
        int cell;
        if (fscanf(fp_in, "%d ", &cell) != 1)
            die("Malformed input file.");
        start[i] = (unsigned char)cell;
        if (cell == 0)
            blankPos = i;
    }
    fclose(fp_in);
    free(line);

    for (int i = 0; i < N - 1; i++)
        goal[i] = (unsigned char)(i + 1);
    goal[N - 1] = 0;

    if (!isSolvable(start)) {
        fprintf(fp_out, "#moves\n");
        fprintf(fp_out, "no solution\n");
        fclose(fp_out);
        free(start);
        free(goal);
        return 0;
    }

    tableSize = 1L << 16;
    tableMask = tableSize - 1;
    table = malloc((size_t)tableSize * sizeof(long));
    if (table == NULL)
        die("Out of memory allocating the visited table.");
    for (long i = 0; i < tableSize; i++)
        table[i] = -1;

    reserveNode();
    memcpy(boards, start, (size_t)N);
    nodes[0].parent = -1;
    nodes[0].tile = 0;
    nodes[0].blank = (unsigned char)blankPos;
    nodeCount = 1;
    tableSeenOrInsert(start, 0);

    long goalIdx = (memcmp(start, goal, (size_t)N) == 0) ? 0 : -1;

    static const int dr[4] = {-1, 1, 0, 0};
    static const int dc[4] = {0, 0, -1, 1};

    unsigned char *child = malloc((size_t)N);
    if (child == NULL)
        die("Out of memory allocating scratch board.");

    long head = 0;
    while (goalIdx == -1 && head < nodeCount) {
        long cur = head++;
        int b = nodes[cur].blank;
        int r = b / k;
        int c = b % k;

        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr < 0 || nr >= k || nc < 0 || nc >= k)
                continue;

            int np = nr * k + nc;

            memcpy(child, boards + (size_t)cur * N, (size_t)N);
            unsigned char moved = child[np];
            child[b] = moved;
            child[np] = 0;

            if (tableSeenOrInsert(child, nodeCount))
                continue;

            reserveNode();
            memcpy(boards + (size_t)nodeCount * N, child, (size_t)N);
            nodes[nodeCount].parent = cur;
            nodes[nodeCount].tile = moved;
            nodes[nodeCount].blank = (unsigned char)np;

            if (memcmp(child, goal, (size_t)N) == 0) {
                goalIdx = nodeCount;
                nodeCount++;
                break;
            }
            nodeCount++;
        }
    }

    fprintf(fp_out, "#moves\n");

    if (goalIdx == -1) {
        fprintf(fp_out, "no solution\n");
    } else {
        long depth = 0;
        for (long i = goalIdx; nodes[i].parent != -1; i = nodes[i].parent)
            depth++;

        unsigned char *moves = malloc((size_t)(depth > 0 ? depth : 1));
        if (moves == NULL)
            die("Out of memory rebuilding the path.");

        long pos = depth;
        for (long i = goalIdx; nodes[i].parent != -1; i = nodes[i].parent)
            moves[--pos] = nodes[i].tile;

        for (long i = 0; i < depth; i++)
            fprintf(fp_out, "%d ", (int)moves[i]);
        fprintf(fp_out, "\n");
        free(moves);
    }

    fclose(fp_out);
    free(child);
    free(table);
    free(nodes);
    free(boards);
    free(start);
    free(goal);
    return 0;
}
