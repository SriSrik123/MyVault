"""Word/digit-generation tree per styleguide sec.6.2: root at top center,
dash-per-unfilled-slot labels, straight edges, dead branches stay visible
(drawn with no children), children ordered increasing left-to-right.
"""
from atoms import R, fmt

ROW_H = 34.0
LEAF_GAP = 8.0


class Node:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children or []


def build(depth, alphabet, valid_prefix, leaf_label=None):
    """Recursively build a tree of given depth over `alphabet` (sorted
    increasing). Every symbol is tried as the next slot (a node is always
    drawn for it); valid_prefix(prefix_tuple) decides only whether that
    node gets further children -- a prefix that fails is drawn as a DEAD
    node (no children), never omitted (styleguide sec.6.2: dead branches
    stay visible). A leaf-level prefix that fails valid_prefix is simply
    not added (not even as dead) since deadness already showed one level
    up wherever it was first detectable.
    leaf_label(prefix_tuple)->str overrides the default digit-join label,
    e.g. to append a slot determined by an earlier choice (2b's digit4).
    Returns the list of depth-1 top nodes."""
    mk_leaf = leaf_label or (lambda p: ''.join(str(c) for c in p))

    def rec(prefix):
        node_children = []
        for a in alphabet:
            p2 = prefix + (a,)
            ok = valid_prefix(p2)
            if len(p2) == depth:
                if ok:
                    node_children.append(Node(mk_leaf(p2), []))
            else:
                dashes = ' '.join(['_'] * (depth - len(p2)))
                lbl = (''.join(str(c) for c in p2) + ' ' + dashes).strip()
                node_children.append(Node(lbl, rec(p2) if ok else []))
        return node_children
    return rec(())


class Tree:
    """A full tree diagram: 'Tree' double-underlined title + root dashes +
    the branching structure. sz sets label font size."""
    def __init__(self, depth, top_nodes, sz=10.5, col_w=52.0):
        self.depth, self.sz, self.col_w = depth, sz, col_w
        self.top_nodes = top_nodes
        self.leaves = []

        def count_leaves(n):
            if not n.children:
                self.leaves.append(n)
                return 1
            return sum(count_leaves(c) for c in n.children)
        for n in top_nodes:
            count_leaves(n)
        n_leaves = max(1, len(self.leaves))
        self.w = max(col_w * n_leaves, col_w * 2)
        self.ht = 14.0   # title sits above baseline y
        self.dp = 20.0 + ROW_H * depth + 14.0

    def emit(self, x, y, show_title=True, root_label=None):
        out = []
        if show_title:
            title = "Tree"
            tw = R(title, self.sz + 1, font='b').w
            tx = x + self.w / 2 - tw / 2
            out += R(title, self.sz + 1, font='b').emit(tx, y)
            out.append(f'\\DLINE{{{fmt(tx)}}}{{{fmt(y + 3)}}}{{{fmt(tx + tw)}}}{{{fmt(y + 3)}}}{{0.5}}')
            out.append(f'\\DLINE{{{fmt(tx)}}}{{{fmt(y + 5)}}}{{{fmt(tx + tw)}}}{{{fmt(y + 5)}}}{{0.5}}')

        root_y = y + 28.0
        root_lbl = root_label if root_label is not None else ' '.join(['_'] * self.depth)
        rw = R(root_lbl, self.sz).w
        root_x = x + self.w / 2
        out += R(root_lbl, self.sz).emit(root_x - rw / 2, root_y)

        leaf_positions = {}
        for i, leaf in enumerate(self.leaves):
            leaf_positions[id(leaf)] = x + self.col_w * (i + 0.5)

        def layout(n, level):
            """returns center-x of this node."""
            ny = root_y + ROW_H * level
            if not n.children:
                cx = leaf_positions[id(n)]
            else:
                child_xs = [layout(c, level + 1) for c in n.children]
                cx = sum(child_xs) / len(child_xs)
            lw = R(n.label, self.sz).w
            out.extend(R(n.label, self.sz).emit(cx - lw / 2, ny))
            n._cx, n._cy = cx, ny
            return cx

        for top in self.top_nodes:
            cx = layout(top, 1)
            out.append(f'\\DLINE{{{fmt(root_x)}}}{{{fmt(root_y + 3)}}}'
                       f'{{{fmt(cx)}}}{{{fmt(top._cy - 9)}}}{{0.5}}')

        def edges(n):
            for c in n.children:
                out.append(f'\\DLINE{{{fmt(n._cx)}}}{{{fmt(n._cy + 3)}}}'
                           f'{{{fmt(c._cx)}}}{{{fmt(c._cy - 9)}}}{{0.5}}')
                edges(c)
        for top in self.top_nodes:
            edges(top)
        return out
