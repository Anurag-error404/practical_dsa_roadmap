"""Tree or graph, depending on the multi-category decision."""


class CategoryNode:
    def __init__(self, name: str):
        self.name = name
        self.children: list["CategoryNode"] = []
        self.product_ids: list[str] = []


class CategoryTree:
    def __init__(self):
        raise NotImplementedError

    def add_category(self, name: str, parent: str | None = None) -> None:
        raise NotImplementedError

    def add_product(self, product_id: str, category: str) -> None:
        raise NotImplementedError

    def products_in(self, category: str, recursive: bool = True) -> list[str]:
        raise NotImplementedError
