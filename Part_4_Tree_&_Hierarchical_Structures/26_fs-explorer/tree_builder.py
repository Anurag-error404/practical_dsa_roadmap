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
