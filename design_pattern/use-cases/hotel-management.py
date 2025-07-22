from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Optional
from datetime import datetime


# Enums

class RoomStyle(Enum):
    STANDARD = "STANDARD"
    DELUX = "DELUX"
    FAMILY_SUITE = "FAMILY_SUITE"


class RoomStatus(Enum):
    AVAILABLE = "AVAILABLE"
    RESERVED = "RESERVED"
    NOT_AVAILABLE = "NOT_AVAILABLE"
    OCCUPIED = "OCCUPIED"
    SERVICE_IN_PROGRESS = "SERVICE_IN_PROGRESS"


class AccountStatus(Enum):
    ACTIVE = "ACTIVE"
    CLOSED = "CLOSED"
    BLOCKED = "BLOCKED"


# Basic Entities

class Location:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude


class Account:
    def __init__(self, username: str, password: str, status: AccountStatus):
        self.username = username
        self.password = password
        self.account_status = status


class Person:
    def __init__(self, name: str, phone: str, account_detail: Account):
        self.name = name
        self.phone = phone
        self.account_detail = account_detail


# Room & Hotel System

class RoomKey:
    def __init__(self, key_id: str, bar_code: str, issued_at: datetime, is_active: bool, is_master: bool):
        self.key_id = key_id
        self.bar_code = bar_code
        self.issued_at = issued_at
        self.is_active = is_active
        self.is_master = is_master

    def assign_room(self, room: 'Room'):
        room.room_keys.append(self)


class HouseKeeper(Person):
    def get_rooms_serviced(self, date: datetime) -> List['Room']:
        # Placeholder logic
        return []


class HouseKeepingLog:
    def __init__(self, description: str, start_date: datetime, duration: int, housekeeper: HouseKeeper):
        self.description = description
        self.start_date = start_date
        self.duration = duration
        self.housekeeper = housekeeper

    def add_house_keeping(self, room: 'Room'):
        room.housekeeping_logs.append(self)


class Room:
    def __init__(self, room_number: str, style: RoomStyle, status: RoomStatus, price: float):
        self.room_number = room_number
        self.room_style = style
        self.room_status = status
        self.booking_price = price
        self.room_keys: List[RoomKey] = []
        self.housekeeping_logs: List[HouseKeepingLog] = []


class Hotel:
    def __init__(self, name: str, hotel_id: int, location: Location):
        self.name = name
        self.id = hotel_id
        self.hotel_location = location
        self.room_list: List[Room] = []


# Booking System

class BookingStatus(Enum):
    REQUESTED = "REQUESTED"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"


class BaseRoomCharge(ABC):
    @abstractmethod
    def get_cost(self) -> float:
        pass


class RoomCharge(BaseRoomCharge):
    def __init__(self, cost: float):
        self._cost = cost

    def get_cost(self) -> float:
        return self._cost

    def set_cost(self, cost: float):
        self._cost = cost


class RoomServiceCharge(BaseRoomCharge):
    def __init__(self, cost: float, base_charge: BaseRoomCharge):
        self.cost = cost
        self.base_charge = base_charge

    def get_cost(self) -> float:
        return self.base_charge.get_cost() + self.cost


class InRoomPurchaseCharges(BaseRoomCharge):
    def __init__(self, cost: float, base_charge: BaseRoomCharge):
        self.cost = cost
        self.base_charge = base_charge

    def get_cost(self) -> float:
        return self.base_charge.get_cost() + self.cost


class RoomBooking:
    def __init__(self, booking_id: str, start_date: datetime, duration: int, booking_status: BookingStatus):
        self.booking_id = booking_id
        self.start_date = start_date
        self.duration_in_days = duration
        self.booking_status = booking_status
        self.guest_list: List['Guest'] = []
        self.room_info: List[Room] = []
        self.total_room_charges: Optional[BaseRoomCharge] = None


class Booking:
    def create_booking(self, guest_info: 'Guest') -> RoomBooking:
        # Placeholder logic
        return RoomBooking("BOOK123", datetime.now(), 2, BookingStatus.CONFIRMED)

    def cancel_booking(self, booking_id: int) -> Optional[RoomBooking]:
        # Placeholder logic
        return None


# User Roles

class Search:
    def search_room(self, room_style: RoomStyle, start_date: datetime, duration: int) -> List[Room]:
        # Placeholder logic
        return []


class Guest(Person):
    def __init__(self, name, phone, account_detail):
        super().__init__(name, phone, account_detail)
        self.search_obj = Search()
        self.booking_obj = Booking()

    def get_all_room_bookings(self) -> List[RoomBooking]:
        return []

    def create_booking(self) -> RoomBooking:
        return self.booking_obj.create_booking(self)

    def cancel_booking(self, booking_id: int) -> Optional[RoomBooking]:
        return self.booking_obj.cancel_booking(booking_id)


class Receptionist(Person):
    def __init__(self, name, phone, account_detail):
        super().__init__(name, phone, account_detail)
        self.search_obj = Search()
        self.booking_obj = Booking()

    def check_in_guest(self, guest: Guest, booking_info: RoomBooking):
        # Placeholder logic
        pass

    def check_out_guest(self, guest: Guest, booking_info: RoomBooking):
        # Placeholder logic
        pass


class Admin(Person):
    def add_room(self, room_detail: Room):
        # Placeholder logic
        pass

    def delete_room(self, room_id: str) -> Optional[Room]:
        # Placeholder logic
        return None

    def edit_room(self, room_detail: Room):
        # Placeholder logic
        pass
