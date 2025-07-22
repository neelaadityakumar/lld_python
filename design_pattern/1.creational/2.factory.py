
from abc import ABC, abstractmethod

# Step 1: Common interface (abstract base class)
class Notification(ABC):
    @abstractmethod
    def notify(self, message: str):
        pass

# Step 2: Concrete implementations
class EmailNotification(Notification):
    def notify(self, message: str):
        print(f"[EMAIL] {message}")

class SMSNotification(Notification):
    def notify(self, message: str):
        print(f"[SMS] {message}")

class PushNotification(Notification):
    def notify(self, message: str):
        print(f"[PUSH] {message}")

# Step 3: Factory method
class NotificationFactory:
    @staticmethod
    def get_notification(method: str) -> Notification:
        if method == "email":
            return EmailNotification()
        elif method == "sms":
            return SMSNotification()
        elif method == "push":
            return PushNotification()
        else:
            raise ValueError("Unknown notification method")


sms_notifier = NotificationFactory.get_notification("sms")
sms_notifier.notify("Your order has been shipped!")

email_notifier = NotificationFactory.get_notification("email")
email_notifier.notify("Check your inbox for confirmation.")

