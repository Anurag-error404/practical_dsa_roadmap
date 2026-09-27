"""Debug printing for any tree shape. Visualization only; it says nothing about correctness.

    print_tree(bst.root, binary_children, lambda n: str(n.value))
    print_tree(trie.root, lambda n: list(n.children.values()), lambda n: "*" if n.is_end else "o")
    print(render_heap(heap.data))
"""
from collections.abc import Callable
from typing import Any


def render_tree(root: Any, children: Callable[[Any], list], label: Callable[[Any], str] = str) -> str:
    """ASCII tree. None children render as a null marker so binary left/right stay distinguishable.

    A node reached twice (e.g. a symlink cycle) is marked with "(seen)" instead of looping forever.
    """
    if root is None:
        return "∅"
    lines, seen = [label(root)], {id(root)}

    # ponytail: recursive, so trees deeper than ~1000 levels hit the recursion limit; switch to an explicit stack if needed
    def walk(node: Any, prefix: str) -> None:
        kids = children(node)
        if all(k is None for k in kids):
            return
        for i, kid in enumerate(kids):
            last = i == len(kids) - 1
            branch = "└── " if last else "├── "
            if kid is None:
                lines.append(prefix + branch + "∅")
            elif id(kid) in seen:
                lines.append(prefix + branch + label(kid) + " (seen)")
            else:
                seen.add(id(kid))
                lines.append(prefix + branch + label(kid))
                walk(kid, prefix + ("    " if last else "│   "))

    walk(root, "")
    return "\n".join(lines)


def print_tree(root: Any, children: Callable[[Any], list], label: Callable[[Any], str] = str) -> None:
    print(render_tree(root, children, label))


def binary_children(node: Any) -> list:
    """children() for nodes with .left/.right."""
    return [node.left, node.right]


def render_heap(data: list) -> str:
    """Array-backed binary heap drawn as its implicit tree (children of i are 2i+1, 2i+2)."""
    if not data:
        return "∅"
    return render_tree(0, lambda i: [c for c in (2 * i + 1, 2 * i + 2) if c < len(data)], lambda i: str(data[i]))


if __name__ == "__main__":
    class N:
        def __init__(self, v, left=None, right=None):
            self.value, self.left, self.right = v, left, right

    t = N(2, N(1), N(3, None, N(4)))
    assert render_tree(t, binary_children, lambda n: str(n.value)) == "2\n├── 1\n└── 3\n    ├── ∅\n    └── 4"
    assert render_heap([1, 2, 3]) == "1\n├── 2\n└── 3"
    loop = N(0)
    loop.left = loop
    assert "(seen)" in render_tree(loop, binary_children, lambda n: str(n.value))
    assert render_tree(None, binary_children) == "∅" and render_heap([]) == "∅"
    print("tree_debug ok")
