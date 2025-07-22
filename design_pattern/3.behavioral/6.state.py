# The State Pattern allows an object to alter its behavior when its internal state changes.
# The object will appear to change its class at runtime.

from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def insert_coin(self, machine):
        pass

    @abstractmethod
    def select_item(self, machine):
        pass

    @abstractmethod
    def dispense(self, machine):
        pass


class IdleState(State):
    def insert_coin(self, machine):
        print("🪙 Coin inserted.")
        machine.set_state(HasMoneyState())

    def select_item(self, machine):
        print("❌ Insert coin first.")

    def dispense(self, machine):
        print("❌ Insert coin and select item first.")


class HasMoneyState(State):
    def insert_coin(self, machine):
        print("❌ Coin already inserted.")

    def select_item(self, machine):
        print("📦 Item selected.")
        machine.set_state(DispensingState())

    def dispense(self, machine):
        print("❌ Select item first.")


class DispensingState(State):
    def insert_coin(self, machine):
        print("❌ Please wait, dispensing in progress.")

    def select_item(self, machine):
        print("❌ Already dispensing item.")

    def dispense(self, machine):
        print("✅ Item dispensed.")
        machine.set_state(IdleState())

class VendingMachine:
    def __init__(self):
        self._state = IdleState()

    def set_state(self, state: State):
        self._state = state

    def insert_coin(self):
        self._state.insert_coin(self)

    def select_item(self):
        self._state.select_item(self)

    def dispense(self):
        self._state.dispense(self)

machine = VendingMachine()

machine.select_item()      # ❌ Insert coin first
machine.insert_coin()      # 🪙 Coin inserted
machine.insert_coin()      # ❌ Coin already inserted
machine.select_item()      # 📦 Item selected
machine.dispense()         # ✅ Item dispensed

# Try a full cycle again
machine.insert_coin()
machine.select_item()
machine.dispense()


