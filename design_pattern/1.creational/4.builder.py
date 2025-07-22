

from enum import Enum

class Size(Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"

class Crust(Enum):
    THIN = "Thin"
    THICK = "Thick"
    CHEESE_STUFFED = "Cheese Stuffed"



class Pizza:
    def __init__(self, size, crust, toppings, extra_cheese):
        self.size = size
        self.crust = crust
        self.toppings = toppings
        self.extra_cheese = extra_cheese

    def __str__(self):
        return (f"Pizza(Size={self.size.value}, Crust={self.crust.value}, "
            f"Toppings={self.toppings}, ExtraCheese={self.extra_cheese})"
        )


class PizzaBuilder:
    def __init__(self):
        self._size = None
        self._crust = None
        self._toppings = []
        self._extra_cheese = False

    def set_size(self, size: Size):
        self._size = size
        return self  # enable chaining

    def set_crust(self, crust: Crust):
        self._crust = crust
        return self

    def add_topping(self, topping: str):
        self._toppings.append(topping)
        return self

    def add_extra_cheese(self):
        self._extra_cheese = True
        return self

    def build(self) -> Pizza:
        # Optional validation
        if not self._size or not self._crust:
            raise ValueError("Size and crust must be selected")
        return Pizza(self._size, self._crust, self._toppings, self._extra_cheese)


pizza = (
    PizzaBuilder()
    .set_size(Size.MEDIUM)
    .set_crust(Crust.CHEESE_STUFFED)
    .add_topping("Onion")
    .add_topping("Jalapeno")
    .add_extra_cheese()
    .build()
)

print(pizza)

