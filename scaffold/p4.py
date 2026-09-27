from textwrap import dedent, indent

from dsl import D, DIRS, P, TRIE_NODE

SHARED = {
    "tree_debug.py": r'''
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
    ''',
}

TRIE_METHODS = r'''
    class Trie:
        def __init__(self):
            self.root = TrieNode()

        def insert(self, word: str) -> None:
            raise NotImplementedError

        def search(self, word: str) -> bool:
            """True only if `word` was inserted as a complete word."""
            raise NotImplementedError

        def starts_with(self, prefix: str) -> bool:
            """True if any inserted word starts with prefix."""
            raise NotImplementedError

        def delete(self, word: str) -> bool:
            """Remove word without breaking other words that share its nodes. Return True if it existed."""
            raise NotImplementedError
'''
TRIE_CLASS = dedent(TRIE_METHODS)

PROJECTS = [
    P(25, "bst", {
        "bst.py": r'''
            """insert/delete/search."""
            from typing import Any


            class TreeNode:
                def __init__(self, value: Any):
                    self.value = value
                    self.left: "TreeNode | None" = None
                    self.right: "TreeNode | None" = None


            class BST:
                def __init__(self):
                    self.root: TreeNode | None = None

                def insert(self, value: Any) -> None:
                    """Insert value. Duplicate policy (reject / right child / count) is yours; be consistent."""
                    raise NotImplementedError

                def delete(self, value: Any) -> None:
                    """Remove value; the tree must still be a valid BST (0, 1, and 2-children cases)."""
                    raise NotImplementedError

                def search(self, value: Any) -> bool:
                    raise NotImplementedError
        ''',
        "traversals.py": r'''
            """In/pre/post-order."""
            from bst import TreeNode


            def inorder(root: TreeNode | None) -> list:
                raise NotImplementedError


            def preorder(root: TreeNode | None) -> list:
                raise NotImplementedError


            def postorder(root: TreeNode | None) -> list:
                raise NotImplementedError
        ''',
        "balance_checker.py": r'''
            """Height-based balance check."""
            from bst import TreeNode


            def height(root: TreeNode | None) -> int:
                """Height of the tree (decide and document: empty tree = 0 or -1)."""
                raise NotImplementedError


            def is_balanced(root: TreeNode | None) -> bool:
                """True if every node's subtree heights differ by at most 1."""
                raise NotImplementedError
        ''',
    }, "tests/test_bst.py", [
        "test_delete_node_with_zero_one_and_two_children",
        "test_delete_root",
        "test_duplicate_insert_policy",
        "test_search_empty_tree",
        "test_delete_missing_value",
        "test_degenerate_tree_flagged_unbalanced",
    ], extra_imports=["from tree_debug import binary_children, print_tree"]),

    P(26, "fs-explorer", {
        "tree_builder.py": r'''
            """Builds an in-memory tree from a real or synthetic file system."""
            from pathlib import Path


            class FSNode:
                def __init__(self, name: str, is_dir: bool, path: str):
                    self.name = name
                    self.is_dir = is_dir
                    self.path = path
                    self.children: list["FSNode"] = []


            def build_tree(root: str | Path) -> FSNode:
                """Walk a real directory into FSNodes. Must survive symlink cycles and permission errors."""
                raise NotImplementedError


            def build_synthetic(spec: dict, name: str = "", path: str = "") -> FSNode:
                """In-memory tree from a nested dict: {"docs": {"a.txt": None}, "empty": {}}. None = file, dict = folder."""
                node = FSNode(name, True, path or "/")
                for child, sub in spec.items():
                    child_path = f"{path}/{child}"
                    node.children.append(
                        build_synthetic(sub, child, child_path) if isinstance(sub, dict) else FSNode(child, False, child_path)
                    )
                return node


            if __name__ == "__main__":
                t = build_synthetic({"docs": {"a.txt": None}, "empty": {}, "b.txt": None})
                assert [c.name for c in t.children] == ["docs", "empty", "b.txt"]
                assert t.children[0].children[0].path == "/docs/a.txt" and not t.children[2].is_dir
                print("tree_builder ok")
        ''',
        "search.py": r'''
            """Name-based search over the tree."""
            from tree_builder import FSNode


            def search(root: FSNode, name: str) -> list[str]:
                """Paths of every file/folder whose name matches."""
                raise NotImplementedError
        ''',
    }, "tests/test_search.py", [
        "test_symlink_cycle_does_not_loop_forever",
        "test_permission_denied_folder_skipped",
        "test_case_sensitivity_policy",
        "test_empty_folders",
        "test_term_matches_both_file_and_folder",
    ], extra_imports=["from tree_debug import print_tree"]),

    P(27, "heap", {
        "heap.py": r'''
            """insert/extract/peek/heapify on an array-backed binary heap."""
            from typing import Any


            class Heap:
                def __init__(self, max_heap: bool = False):
                    """Min-heap by default; max_heap=True flips the ordering."""
                    self.max_heap = max_heap
                    self.data: list = []

                @classmethod
                def heapify(cls, items: list, max_heap: bool = False) -> "Heap":
                    """Build a heap from an unsorted list in O(n) (sift-down from the last parent, not n inserts)."""
                    raise NotImplementedError

                def insert(self, value: Any) -> None:
                    raise NotImplementedError

                def extract(self) -> Any:
                    """Remove and return the min (or max, for a max-heap)."""
                    raise NotImplementedError

                def peek(self) -> Any:
                    raise NotImplementedError

                def __len__(self) -> int:
                    raise NotImplementedError
        ''',
    }, "tests/test_heap.py", [
        "test_extract_on_empty_heap",
        "test_single_element_heap",
        "test_duplicate_values",
        "test_sift_at_root_and_last_leaf_boundaries",
        "test_heapify_is_linear_not_repeated_insert",
    ], extra_imports=["from tree_debug import render_heap"]),

    DIRS(28, "leaderboard-or-huffman",
        D("A_leaderboard", {
            "leaderboard.py": r'''
                """Heap + hash map: O(log n) update, O(k) top-k read."""


                class Leaderboard:
                    def __init__(self):
                        raise NotImplementedError

                    def update(self, user: str, score: float) -> None:
                        """Set user's score. Repeated updates move the user, never duplicate them."""
                        raise NotImplementedError

                    def top_k(self, k: int) -> list[tuple[str, float]]:
                        """Current top k (user, score), best first."""
                        raise NotImplementedError
            ''',
        }, "tests/test_leaderboard.py", [
            "test_repeated_user_update_moves_not_duplicates",
            "test_score_ties_follow_defined_rule",
            "test_k_larger_than_user_count_returns_everyone",
        ], edge=0),
        D("B_huffman-compressor", {
            "huffman_tree.py": r'''
                class HuffmanNode:
                    def __init__(self, freq: int, symbol: int | None = None,
                                 left: "HuffmanNode | None" = None, right: "HuffmanNode | None" = None):
                        self.freq = freq
                        self.symbol = symbol
                        self.left = left
                        self.right = right


                def build_tree(data: bytes) -> HuffmanNode | None:
                    """Huffman tree from byte frequencies (built with a heap)."""
                    raise NotImplementedError


                def build_codes(root: HuffmanNode | None) -> dict[int, str]:
                    """Byte value -> bit string."""
                    raise NotImplementedError
            ''',
            "encoder.py": r'''
                def encode(data: bytes) -> bytes:
                    """Compressed bytes, including whatever header decode() needs to rebuild the tree."""
                    raise NotImplementedError
            ''',
            "decoder.py": r'''
                def decode(blob: bytes) -> bytes:
                    """Exact inverse of encode()."""
                    raise NotImplementedError
            ''',
        }, "tests/test_roundtrip.py", [
            "test_single_distinct_symbol_input",
            "test_empty_input",
            "test_roundtrip_is_byte_identical",
        ], edge=1, extra_imports=["from tree_debug import binary_children, print_tree"]),
    ),

    P(29, "trie", {
        "trie.py": "\"\"\"insert/search/starts_with/delete.\"\"\"\n\n" + TRIE_NODE + "\n" + TRIE_CLASS,
    }, "tests/test_trie.py", [
        "test_delete_word_that_prefixes_another_keeps_shared_nodes",
        "test_insert_empty_string",
        "test_case_sensitivity_policy",
        "test_internal_prefix_starts_with_true_search_false",
        "test_delete_word_never_inserted",
    ], extra_imports=["from tree_debug import print_tree"]),

    P(30, "autocomplete", {
        "trie.py": "\"\"\"Copy in your Project 29 trie, then extend it.\"\"\"\n\n" + TRIE_NODE + "\n" + TRIE_CLASS + indent(dedent(r'''
            def words_with_prefix(self, prefix: str) -> list[str]:
                """Every stored word starting with prefix."""
                raise NotImplementedError
        '''), "    "),
        "ranker.py": r'''
            """Frequency-based suggestion ranking."""


            class Ranker:
                def __init__(self, frequencies: dict[str, int] | None = None):
                    raise NotImplementedError

                def record_use(self, word: str) -> None:
                    """Optional: bump a word's rank when it's used."""
                    raise NotImplementedError

                def rank(self, words: list[str], limit: int) -> list[str]:
                    """The best `limit` words, most useful first."""
                    raise NotImplementedError
        ''',
        "api.py": r'''
            """query(prefix) -> ranked suggestions."""
            from collections.abc import Iterable
            from pathlib import Path

            from ranker import Ranker
            from trie import Trie


            def load_words(path: str | Path) -> list[str]:
                """One word per line; blank lines skipped."""
                return [w for line in Path(path).read_text().splitlines() if (w := line.strip())]


            class Autocomplete:
                def __init__(self, words: Iterable[str], frequencies: dict[str, int] | None = None):
                    self.trie = Trie()
                    for w in words:
                        self.trie.insert(w)
                    self.ranker = Ranker(frequencies)

                def query(self, prefix: str, limit: int = 10) -> list[str]:
                    """Up to `limit` ranked completions of prefix. No matches: empty list."""
                    raise NotImplementedError
        ''',
    }, "tests/test_autocomplete.py", [
        "test_no_matches_returns_empty_list",
        "test_short_prefix_capped_and_ranked",
        "test_case_mismatch_between_input_and_dictionary",
        "test_ranking_updates_with_usage",
    ]),
]
