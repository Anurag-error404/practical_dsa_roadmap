from dataclasses import dataclass, field


@dataclass
class Product:
    id: str
    name: str
    price: float
    rating: float | None = None
    categories: list[str] = field(default_factory=list)


@dataclass
class Bundle:
    products: list[Product] = field(default_factory=list)
    total_price: float = 0.0
    total_value: float = 0.0
    message: str = ""
