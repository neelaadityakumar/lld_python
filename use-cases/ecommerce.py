from typing import List, Optional
from enum import Enum
from datetime import date


class Customer:
    def __init__(self, customer_id: int):
        self.cart: Optional[ShoppingCart] = None
        self.search_obj: Optional[Search] = None
        self.customer_id = customer_id

    def get_shopping_cart(self, customer_id: int) -> Optional['ShoppingCart']:
        return self.cart

    def add_items_to_shopping_cart(self, item: 'Item'):
        pass

    def update_item_from_shopping_cart(self, item: 'Item'):
        pass

    def remove_item_from_shopping_cart(self, item: 'Item'):
        pass


class Guest(Customer):
    def create_new_account(self) -> 'Account':
        pass


class User(Customer):
    def __init__(self, customer_id: int):
        super().__init__(customer_id)
        self.account: Optional[Account] = None


class Seller(User):
    def add_product(self, product: 'Product'):
        pass


class Buyer(User):
    def __init__(self, customer_id: int):
        super().__init__(customer_id)
        self.order_obj: Optional[Order] = None

    def add_review(self, review: 'ProductReview'):
        pass

    def place_order(self, cart: 'ShoppingCart') -> 'OrderStatus':
        pass


class Account:
    def __init__(self):
        self.name: str = ""
        self.email: str = ""
        self.phone_number: str = ""
        self.user_name: str = ""
        self.password: str = ""
        self.shipping_addresses: List['Address'] = []
        self.account_status: Optional['AccountStatus'] = None


class Address:
    def __init__(self):
        self.pin_code: int = 0
        self.street: str = ""
        self.city: str = ""
        self.state: str = ""
        self.country: str = ""


class AccountStatus(Enum):
    ACTIVE = 1
    BLOCKED = 2
    INACTIVE = 3


class ShoppingCart:
    def __init__(self):
        self.items: List['Item'] = []
        self.cart_value: float = 0.0

    def add_item(self, item: 'Item'):
        pass

    def update_item(self, item: 'Item'):
        pass

    def delete_item(self, item: 'Item'):
        pass

    def checkout_items(self):
        pass

    def get_items(self) -> List['Item']:
        return self.items

    def get_cart_value(self) -> float:
        return self.cart_value


class Item:
    def __init__(self):
        self.product: Optional['Product'] = None
        self.qty: int = 0


class Product:
    def __init__(self):
        self.product_id: int = 0
        self.product_description: str = ""
        self.name: str = ""
        self.product_category: Optional['ProductCategory'] = None
        self.seller: Optional[Seller] = None
        self.cost: float = 0.0
        self.product_reviews: List['ProductReview'] = []


class ProductCategory(Enum):
    ELECTRONICS = 1
    FURNITURE = 2
    GROCERY = 3
    MOBILE = 4


class ProductReview:
    def __init__(self):
        self.details: str = ""
        self.reviewer: Optional[Buyer] = None
        self.rating: int = 0


class Search:
    def search_by_name(self, name: str) -> List[Product]:
        pass

    def search_by_category(self, category: ProductCategory) -> List[Product]:
        pass


class Order:
    def __init__(self):
        self.order_id: int = 0
        self.order_item: List[Item] = []
        self.order_value: float = 0.0
        self.buyer: Optional[Buyer] = None
        self.order_date: Optional[date] = None
        self.notification_service: Optional['NotificationService'] = None
        self.order_log: List['OrderLog'] = []

    def place_order(self) -> 'OrderStatus':
        pass

    def track_order(self) -> 'OrderStatus':
        pass

    def add_order_logs(self):
        pass

    def make_payment(self, payment_type: 'PaymentType') -> 'PaymentStatus':
        pass


class OrderStatus(Enum):
    PACKED = 1
    SHIPPED = 2
    ENROUTE = 3
    OUT_FOR_DELIVERY = 4
    DELIVERED = 5
    CANCELLED = 6


class PaymentStatus(Enum):
    SUCCESS = 1
    ERROR = 2
    CANCELLED = 3
    REFUND_INITIATED = 4
    REFUNDED = 5


class PaymentType(Enum):
    CREDIT_CARD = 1
    DEBIT_CARD = 2
    NET_BANKING = 3
    UPI = 4


class OrderLog:
    def __init__(self):
        self.order_detail: str = ""
        self.created_date: Optional[date] = None
        self.status: Optional[OrderStatus] = None


class NotificationDomain:
    def __init__(self):
        self.notification_id: str = ""
        self.notification_type: Optional['NotificationType'] = None
        self.user: Optional[User] = None


class NotificationType(Enum):
    EMAIL = 1
    WHATSAPP = 2
    SMS = 3


class NotificationService:
    def send_notification(self, notification_domain: NotificationDomain) -> bool:
        notification_object: Optional[Notification] = None
        message_attribute: Optional[MessageAttributes] = None

        if notification_domain.notification_type == NotificationType.EMAIL:
            notification_object = EmailNotification()
            message_attribute = MessageAttributes("abc@abc.com", notification_domain.user.account.email, "Order Detail ...")
        elif notification_domain.notification_type == NotificationType.WHATSAPP:
            notification_object = WhatsappNotification()
            message_attribute = MessageAttributes("9888888888", notification_domain.user.account.phone_number, "Order Detail ...")
        else:
            notification_object = SMSNotification()
            message_attribute = MessageAttributes("988888888", notification_domain.user.account.phone_number, "Order Detail ...")

        return notification_object.send_notification(message_attribute)


class MessageAttributes:
    def __init__(self, to: str, from_: str, message: str):
        self.to = to
        self.from_ = from_
        self.message = message


class Notification:
    def send_notification(self, message_attribute: MessageAttributes) -> bool:
        raise NotImplementedError


class EmailNotification(Notification):
    def send_notification(self, message_attribute: MessageAttributes) -> bool:
        return True


class WhatsappNotification(Notification):
    def send_notification(self, message_attribute: MessageAttributes) -> bool:
        return True


class SMSNotification(Notification):
    def send_notification(self, message_attribute: MessageAttributes) -> bool:
        return True
