# The Specification Pattern allows you to encapsulate business rules or filter criteria in reusable, combinable, and
# testable objects, instead of scattering if-else logic across your codebase.

from abc import ABC, abstractmethod

class Specification(ABC):
    @abstractmethod
    def is_satisfied(self, item) -> bool:
        pass

    def __and__(self, other):
        return AndSpecification(self, other)

    def __or__(self, other):
        return OrSpecification(self, other)

    def __invert__(self):
        return NotSpecification(self)


class AndSpecification(Specification):
    def __init__(self, *specs):
        self.specs = specs

    def is_satisfied(self, item):
        return all(spec.is_satisfied(item) for spec in self.specs)


class OrSpecification(Specification):
    def __init__(self, *specs):
        self.specs = specs

    def is_satisfied(self, item):
        return any(spec.is_satisfied(item) for spec in self.specs)


class NotSpecification(Specification):
    def __init__(self, spec):
        self.spec = spec

    def is_satisfied(self, item):
        return not self.spec.is_satisfied(item)


class Product:
    def __init__(self, name: str, category: str, price: float):
        self.name = name
        self.category = category
        self.price = price

    def __repr__(self):
        return f"{self.name} (${self.price}, {self.category})"


class PriceUnder(Specification):
    def __init__(self, max_price):
        self.max_price = max_price

    def is_satisfied(self, product):
        return product.price < self.max_price


class CategoryIs(Specification):
    def __init__(self, category):
        self.category = category

    def is_satisfied(self, product):
        return product.category.lower() == self.category.lower()


class ProductFilter:
    def filter(self, items, spec: Specification):
        return [item for item in items if spec.is_satisfied(item)]


products = [
    Product("iPhone", "Electronics", 999),
    Product("Shoes", "Clothing", 80),
    Product("MacBook", "Electronics", 1500),
    Product("T-Shirt", "Clothing", 25),
    Product("Headphones", "Electronics", 150)
]

pf = ProductFilter()

cheap = PriceUnder(100)
electronics = CategoryIs("Electronics")

print("🛍️ Cheap Products (< ₹100):")
print(pf.filter(products, cheap))

print("\n🎧 Cheap Electronics:")
print(pf.filter(products, cheap | electronics))

print("\n🧢 Non-Electronics:")
print(pf.filter(products, ~electronics))

