"""Public API: browse / filter / sort / bundle_suggest."""
from collections.abc import Iterable

from bundle_optimizer import suggest_bundle
from category_tree import CategoryTree
from filter_sort import filter_by_price, sort_products
from models import Bundle, Product
from product_store import ProductStore


class Catalogue:
    def __init__(self, products: Iterable[Product] = ()):
        self.store = ProductStore()
        self.categories = CategoryTree()
        for p in products:
            self.add_product(p)

    def add_product(self, product: Product) -> None:
        raise NotImplementedError

    def browse(self, category: str) -> list[Product]:
        raise NotImplementedError

    def filter(self, lo: float, hi: float) -> list[Product]:
        raise NotImplementedError

    def sort(self, products: list[Product], criteria: list[str]) -> list[Product]:
        raise NotImplementedError

    def bundle_suggest(self, budget: float) -> Bundle:
        raise NotImplementedError
