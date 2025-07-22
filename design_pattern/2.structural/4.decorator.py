# The Decorator Pattern allows you to dynamically add new behaviors to objects without modifying their structure or code.
from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass


class Margherita(Pizza):
    def get_description(self) -> str:
        return "Margherita Pizza"

    def get_cost(self) -> float:
        return 200.0


class ToppingDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self._pizza = pizza


class ExtraCheese(ToppingDecorator):
    def get_description(self) -> str:
        return self._pizza.get_description() + ", Extra Cheese"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + 40.0

class Olives(ToppingDecorator):
    def get_description(self) -> str:
        return self._pizza.get_description() + ", Olives"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + 30.0


pizza = Margherita()
print(pizza.get_description(), "-", pizza.get_cost())

# Add extra cheese
pizza_with_cheese = ExtraCheese(pizza)
print(pizza_with_cheese.get_description(), "-", pizza_with_cheese.get_cost())

# Add olives on top of cheese
final_pizza = Olives(pizza_with_cheese)
print(final_pizza.get_description(), "-", final_pizza.get_cost())

