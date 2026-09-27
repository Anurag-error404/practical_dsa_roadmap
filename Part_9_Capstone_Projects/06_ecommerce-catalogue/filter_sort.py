"""Two-pointer/sliding-window range filter plus multi-key sort."""
from models import Product


def filter_by_price(products_by_price: list[Product], lo: float, hi: float) -> list[Product]:
    """Products with lo <= price <= hi, given a list already sorted by price."""
    raise NotImplementedError


def sort_products(products: list[Product], criteria: list[str]) -> list[Product]:
    """Multi-key sort, e.g. ["-rating", "price"]."""
    raise NotImplementedError
