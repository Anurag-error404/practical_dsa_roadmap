"""Hashing for product lookup. Storage only."""
from models import Product


class ProductStore:
    def __init__(self):
        self._by_id: dict[str, Product] = {}

    def add(self, product: Product) -> None:
        self._by_id[product.id] = product

    def get(self, product_id: str) -> Product:
        return self._by_id[product_id]

    def all(self) -> list[Product]:
        return list(self._by_id.values())

    def __len__(self) -> int:
        return len(self._by_id)
