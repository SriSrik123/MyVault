# Closed Hash Tables & Trees — CS260 (Day 8)
**Date:** 2026-07-15
**Source:** CS260 day 8.pdf (handwritten + slides)

## Overview
Finished hash tables by covering closed hashing (rehashing strategies) and resizing, then introduced Trees as an ADT — terminology, tree walks (preorder/inorder/postorder), and recursive functions for counting nodes and computing height.

## Key Concepts

### Closed Hash Tables
- Uses one array of values (no linked lists, unlike open hashing).
- Collisions are handled with a **rehash strategy** instead of chaining.
- If the table is full, options are: rewrite, overwrite, or throw an error.

**Rehashing strategies:**
1. **Linear Probing:** `h_k(v,N) = (h(v,N) + k) mod N` — keep checking the next slot until a free one is found; k = number of hashing attempts.
2. **Quadratic Probing:** `h_k(v,N) = (h(v,N) + c1*k + c2*k²) mod N` — jumps around by k² instead of checking sequentially; c1, c2 are constants.
3. **Double Hashing:** `h_k(v,N) = (h1(v) + k*h2(v)) mod N` — uses two separate hash functions. Doesn't fully solve the collision problem, just reduces it.

### Closed Hash Table Resize
- When out of space, resize by doubling the table size and rehashing every element into the new table.
- `resize()` walks the old table, reinserts each non-empty slot into a new table of size `oldSize*2`, then frees the old table.
- Worked example: resizing a 10-slot table to 20 slots and reinserting all elements.
- Why resize instead of alternatives? One reason given: when you only need the most recent elements.

### Trees (ADT)
- An empty/null tree has nothing in it; a single node is also a valid tree.
- A **node** is an element in a tree; a **parent** connects to a **child** via an **edge** (e.g., edge (3,10) means 3 is parent of 10).
- **Leaf:** a node with no children.
- **Node height:** max number of edges from that node to a leaf.
- **Node depth:** number of edges from that node to the root.
- **Path:** a sequence of connected nodes.
- **Unary tree:** each node has 1 child (equivalent to a linked list).
- **N-ary tree:** each node has at most N children.

### Recursion Revisit — Tree = Recursion
Tree walks:
- **Preorder:** print node, then visit left children, then visit right (go all the way down first).
- **Inorder:** visit left, print node, visit right (go all the way left first).
- **Postorder:** visit left, visit right, then print node.
- Runtime for a full tree walk is always O(N).

Recursive inorder walk example:
```c
void inorderWalk(Node *node)
{
    if (node != NULL)
    {
        inorderWalk(node->left);
        print(node->value);
        inorderWalk(node->right);
    }
}
```

### Practice Problems Introduced
- **Perfect tree:** all nulls on the same level, no missing spaces at any level.
  - Q1: given height h, how many nodes exist (in terms of h)?
  - Q2: given n nodes, what is the height (in terms of n)?
- **Count nodes in a binary tree** — recursive function `int countNodes(struct Node* root)`.
- **Height of a binary tree** — recursive function `int treeHeight(struct Node* root)`; height of a single-node tree is 0, defined as the number of edges on the longest root-to-leaf path.

## Summary
Closed hash tables trade the linked-list buckets of open hashing for probing strategies (linear, quadratic, double hashing) within a single array, and rely on doubling + rehashing to grow. The lecture then pivoted to trees as a new ADT, framing tree traversal as a direct application of recursion (preorder/inorder/postorder), and set up practice problems on node counting and height calculation to reinforce writing recursive tree functions.
