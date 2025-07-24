from typing import List, Dict
from datetime import datetime
from enum import Enum


class ParkingLot:
    def __init__(self):
        self.parking_floors: List[ParkingFloor] = []
        self.entrances: List['Entrance'] = []
        self.exits: List['Exit'] = []
        self.address: 'Address' = None
        self.parking_lot_name: str = ""

    def is_parking_space_available_for_vehicle(self, vehicle: 'Vehicle') -> bool:
        pass

    def update_parking_attendant(self, parking_attendant: 'ParkingAttendant', gate_id: int) -> bool:
        pass


class ParkingFloor:
    def __init__(self):
        self.level_id: int = 0
        self.parking_spaces: List['ParkingSpace'] = []
        self.parking_display_board: 'ParkingDisplayBoard' = None


class Gate:
    def __init__(self):
        self.gate_id: int = 0
        self.parking_attendant: 'ParkingAttendant' = None


class Entrance(Gate):
    def get_parking_ticket(self, vehicle: 'Vehicle') -> 'ParkingTicket':
        pass


class Exit(Gate):
    def pay_for_parking(self, parking_ticket: 'ParkingTicket', payment_type: 'PaymentType') -> 'ParkingTicket':
        pass


class Address:
    def __init__(self):
        self.country: str = ""
        self.state: str = ""
        self.city: str = ""
        self.street: str = ""
        self.pin_code: str = ""  # ZipCode


class ParkingSpace:
    def __init__(self):
        self.space_id: int = 0
        self.is_free: bool = True
        self.cost_per_hour: float = 0.0
        self.vehicle: 'Vehicle' = None
        self.parking_space_type: 'ParkingSpaceType' = None


class ParkingDisplayBoard:
    def __init__(self):
        self.free_spots_available_map: Dict['ParkingSpaceType', int] = {}

    def update_free_spots_available(self, parking_space_type: 'ParkingSpaceType', spaces: int):
        pass


class Account:
    def __init__(self):
        self.name: str = ""
        self.email: str = ""
        self.password: str = ""
        self.emp_id: str = ""
        self.address: 'Address' = None


class Admin(Account):
    def add_parking_floor(self, parking_lot: ParkingLot, floor: ParkingFloor) -> bool:
        pass

    def add_parking_space(self, floor: ParkingFloor, parking_space: ParkingSpace) -> bool:
        pass

    def add_parking_display_board(self, floor: ParkingFloor, parking_display_board: ParkingDisplayBoard) -> bool:
        pass

    # ... more methods as in Java


class ParkingAttendant(Account):
    def __init__(self):
        super().__init__()
        self.payment_service: 'Payment' = None

    def process_vehicle_entry(self, vehicle: 'Vehicle') -> bool:
        pass

    def process_payment(self, parking_ticket: 'ParkingTicket', payment_type: 'PaymentType') -> 'PaymentInfo':
        pass


class Vehicle:
    def __init__(self):
        self.license_number: str = ""
        self.vehicle_type: 'VehicleType' = None
        self.parking_ticket: 'ParkingTicket' = None
        self.payment_info: 'PaymentInfo' = None


class ParkingTicket:
    def __init__(self):
        self.ticket_id: int = 0
        self.level_id: int = 0
        self.space_id: int = 0
        self.vehicle_entry_date_time: datetime = None
        self.vehicle_exit_date_time: datetime = None
        self.parking_space_type: 'ParkingSpaceType' = None
        self.total_cost: float = 0.0
        self.parking_ticket_status: 'ParkingTicketStatus' = None

    def update_total_cost(self):
        pass

    def update_vehicle_exit_time(self, vehicle_exit_date_time: datetime):
        pass


class Payment:
    def make_payment(self, parking_ticket: ParkingTicket, payment_type: 'PaymentType') -> 'PaymentInfo':
        pass


class PaymentInfo:
    def __init__(self):
        self.amount: float = 0.0
        self.payment_date: datetime = None
        self.transaction_id: int = 0
        self.parking_ticket: ParkingTicket = None
        self.payment_status: 'PaymentStatus' = None


class PaymentType(Enum):
    CASH = 1
    CREDIT_CARD = 2
    DEBIT_CARD = 3
    UPI = 4


class ParkingSpaceType(Enum):
    BIKE_PARKING = 1
    CAR_PARKING = 2
    TRUCK_PARKING = 3


class VehicleType(Enum):
    BIKE = 1
    CAR = 2
    TRUCK = 3


class ParkingTicketStatus(Enum):
    PAID = 1
    ACTIVE = 2


class PaymentStatus(Enum):
    UNPAID = 1
    PENDING = 2
    COMPLETED = 3
    DECLINED = 4
    CANCELLED = 5
    REFUNDED = 6
