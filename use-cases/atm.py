from abc import ABC, abstractmethod
from datetime import date
from enum import Enum
from typing import List, Dict


class ATM:
    def __init__(self, atm_id: int, location: 'Address'):
        self.atm_id = atm_id
        self.location = location
        self.cash_dispenser = CashDispenser()
        self.screen = Screen()
        self.card_reader = CardReader()
        self.keypad = Keypad()
        self.cash_deposit = CashDeposit()
        self.cheque_deposit = ChequeDeposit()
        self.bank_service: BankService = None


class Address:
    def __init__(self, pin_code: int, street: str, city: str, state: str, country: str):
        self.pin_code = pin_code
        self.street = street
        self.city = city
        self.state = state
        self.country = country


class CashType(Enum):
    FIFTY = 50
    HUNDRED = 100
    FIVEHUNDRED = 500


class Cash:
    def __init__(self, cash_type: CashType, serial_number: str):
        self.cash_type = cash_type
        self.serial_number = serial_number


class CashDispenser:
    def __init__(self):
        self.cash_available: Dict[CashType, List[Cash]] = {}

    def dispense_cash(self, amount: int):
        pass


class Screen:
    def display(self, message: str):
        pass


class CardType(Enum):
    DEBIT = "DEBIT"
    CREDIT = "CREDIT"


class CardInfo:
    def __init__(self, card_type: CardType, bank: 'Bank', card_number: str, expiry_date: date, cvv: int, withdraw_limit: float):
        self.card_type = card_type
        self.bank = bank
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv
        self.withdraw_limit = withdraw_limit


class CardReader:
    def fetch_card_details(self) -> CardInfo:
        pass


class Keypad:
    def get_input(self) -> str:
        pass


class Bank:
    def __init__(self, name: str, location: Address):
        self.name = name
        self.location = location
        self.atm_list: List[ATM] = []


class BankService(ABC):
    @abstractmethod
    def is_valid_user(self, pin: str, card_info: CardInfo) -> bool:
        pass

    @abstractmethod
    def get_customer_details(self, card_info: CardInfo) -> 'Customer':
        pass

    @abstractmethod
    def execute_transaction(self, transaction_info: 'Transaction', customer: 'Customer') -> 'TransactionDetail':
        pass


class BankA(BankService):
    def is_valid_user(self, pin: str, card_info: CardInfo) -> bool:
        pass

    def get_customer_details(self, card_info: CardInfo) -> 'Customer':
        pass

    def execute_transaction(self, transaction_info: 'Transaction', customer: 'Customer') -> 'TransactionDetail':
        pass


class BankB(BankService):
    def is_valid_user(self, pin: str, card_info: CardInfo) -> bool:
        pass

    def get_customer_details(self, card_info: CardInfo) -> 'Customer':
        pass

    def execute_transaction(self, transaction_info: 'Transaction', customer: 'Customer') -> 'TransactionDetail':
        pass


class BankServiceFactory:
    def get_bank_service_object(self, card_info: CardInfo) -> BankService:
        pass


class CustomerStatus(Enum):
    BLOCKED = "BLOCKED"
    ACTIVE = "ACTIVE"
    CLOSED = "CLOSED"


class Account:
    def __init__(self, account_number: str, available_balance: float):
        self.account_number = account_number
        self.available_balance = available_balance


class Customer:
    def __init__(self, first_name: str, last_name: str, account_number: str, card_info: CardInfo, account: Account):
        self.first_name = first_name
        self.last_name = last_name
        self.account_number = account_number
        self.card_info = card_info
        self.account = account
        self.bank_service_obj: BankService = None
        self.customer_status = CustomerStatus.ACTIVE


class Transaction:
    def __init__(self, transaction_id: int, source_account: str, transaction_date: date):
        self.transaction_id = transaction_id
        self.source_account = source_account
        self.transaction_date = transaction_date


class Deposit(Transaction):
    def __init__(self, transaction_id: int, source_account: str, transaction_date: date, amount: float):
        super().__init__(transaction_id, source_account, transaction_date)
        self.amount = amount


class ChequeDeposit(Deposit):
    def get_cheque(self):
        pass


class CashDeposit(Deposit):
    def get_cash(self) -> List[Cash]:
        pass


class Withdraw(Transaction):
    def __init__(self, transaction_id: int, source_account: str, transaction_date: date, amount: float):
        super().__init__(transaction_id, source_account, transaction_date)
        self.amount = amount


class Transfer(Transaction):
    def __init__(self, transaction_id: int, source_account: str, transaction_date: date, dest_account: str, amount: float):
        super().__init__(transaction_id, source_account, transaction_date)
        self.dest_account = dest_account
        self.amount = amount


class TransactionStatus(Enum):
    PENDING = "PENDING"
    CANCELLED = "CANCELLED"
    SUCCESS = "SUCCESS"
    ERROR = "ERROR"


class TransactionType(Enum):
    WITHDRAW = "WITHDRAW"
    DEPOSIT = "DEPOSIT"
    TRANSFER = "TRANSFER"


class TransactionDetail:
    def __init__(self, transaction_status: TransactionStatus, source_account_number: str,
                 transaction_date: date, transaction_type: TransactionType, transaction_id: int):
        self.transaction_status = transaction_status
        self.source_account_number = source_account_number
        self.transaction_date = transaction_date
        self.transaction_type = transaction_type
        self.transaction_id = transaction_id
