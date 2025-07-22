# The Strategy Pattern allows you to define a family of algorithms, encapsulate each one, and make them interchangeable.
# The strategy lets the algorithm vary independently from the clients that use it.


from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass


class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str):
        self.card_number = card_number

    def pay(self, amount: float):
        print(f"💳 Paid ₹{amount} using Credit Card: {self.card_number}")


class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float):
        print(f"📧 Paid ₹{amount} using PayPal account: {self.email}")


class UPIPayment(PaymentStrategy):
    def __init__(self, upi_id: str):
        self.upi_id = upi_id

    def pay(self, amount: float):
        print(f"📱 Paid ₹{amount} using UPI ID: {self.upi_id}")


class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def process_payment(self, amount: float):
        self._strategy.pay(amount)


# Use UPI
upi_payment = UPIPayment("aditya@upi")
context = PaymentContext(upi_payment)
context.process_payment(499.0)

# Switch to Credit Card
card_payment = CreditCardPayment("1234-5678-9876-5432")
context.set_strategy(card_payment)
context.process_payment(1250.0)

# Switch to PayPal
paypal = PayPalPayment("aditya@example.com")
context.set_strategy(paypal)
context.process_payment(750.0)

