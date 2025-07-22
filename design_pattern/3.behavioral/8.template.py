# The Template Method Pattern defines an algorithm in a base (abstract) class, deferring some steps to subclasses.
#  It lets subclasses redefine specific parts of the algorithm without changing its structure.


from abc import ABC, abstractmethod

class Beverage(ABC):
    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("💧 Boiling water")

    @abstractmethod
    def brew(self):
        pass

    def pour_in_cup(self):
        print("☕ Pouring into cup")

    @abstractmethod
    def add_condiments(self):
        pass


class Tea(Beverage):
    def brew(self):
        print("🫖 Steeping the tea")

    def add_condiments(self):
        print("🍋 Adding lemon")


class Coffee(Beverage):
    def brew(self):
        print("☕ Brewing the coffee grounds")

    def add_condiments(self):
        print("🧂 Adding sugar and milk")


print("Preparing Tea:")
tea = Tea()
tea.prepare()

print("\nPreparing Coffee:")
coffee = Coffee()
coffee.prepare()

