from typing import List, Optional
from datetime import date
from enum import Enum
from abc import ABC, abstractmethod


class Hotel:
    def __init__(self, name: str, id: int, hotel_location: 'Location', room_list: List['Room']):
        self.name = name
        self.id = id
        self.hotel_location = hotel_location
        self.room_list = room_list


class Location:
    def __init__(self, longitude: float, latitude: float):
        self.longitude = longitude
        self.latitude = latitude


class Room:
    def __init__(self, room_number: str, room_style: 'RoomStyle', room_status: 'RoomStatus',
                 booking_price: float, room_keys: List['RoomKey'], house_keeping_logs: List['HouseKeepingLog']):
        self.room_number = room_number
        self.room_style = room_style
        self.room_status = room_status
        self.booking_price = booking_price
        self.room_keys = room_keys
        self.house_keeping_logs = house_keeping_logs


class RoomStyle(Enum):
    STANDARD = 1
    DELUX = 2
    FAMILY_SUITE = 3


class RoomStatus(Enum):
    AVAILABLE = 1
    RESERVED = 2
    NOT_AVAILABLE = 3
    OCCUPIED = 4
    SERVICE_IN_PROGRESS = 5


class RoomKey:
    def __init__(self, key_id: str, bar_code: str, issued_at: date, is_active: bool, is_master: bool):
        self.key_id = key_id
        self.bar_code = bar_code
        self.issued_at = issued_at
        self.is_active = is_active
        self.is_master = is_master

    def assign_room(self, room: Room):
        self.room = room


class HouseKeepingLog:
    def __init__(self, description: str, start_date: date, duration: int, housekeeper: 'HouseKeeper'):
        self.description = description
        self.start_date = start_date
        self.duration = duration
        self.housekeeper = housekeeper

    def add_room(self, room: Room):
        self.room = room


class Person:
    def __init__(self, name: str, account_detail: 'Account', phone: str):
        self.name = name
        self.account_detail = account_detail
        self.phone = phone


class Account:
    def __init__(self, username: str, password: str, account_status: 'AccountStatus'):
        self.username = username
        self.password = password
        self.account_status = account_status


class AccountStatus(Enum):
    ACTIVE = 1
    CLOSED = 2
    BLOCKED = 3


class HouseKeeper(Person):
    def get_rooms_serviced(self, date: date) -> List[Room]:
        pass


class Guest(Person):
    def __init__(self, name: str, account_detail: 'Account', phone: str,
                 search_obj: 'Search', booking_obj: 'Booking'):
        super().__init__(name, account_detail, phone)
        self.search_obj = search_obj
        self.booking_obj = booking_obj

    def get_all_room_bookings(self) -> List['RoomBooking']:
        pass

    def create_booking(self) -> 'RoomBooking':
        pass

    def cancel_booking(self, booking_id: int) -> 'RoomBooking':
        pass


class Receptionist(Person):
    def __init__(self, name: str, account_detail: 'Account', phone: str,
                 search_obj: 'Search', booking_obj: 'Booking'):
        super().__init__(name, account_detail, phone)
        self.search_obj = search_obj
        self.booking_obj = booking_obj

    def check_in_guest(self, guest: Guest, booking_info: 'RoomBooking'):
        pass

    def check_out_guest(self, guest: Guest, booking_info: 'RoomBooking'):
        pass


class Admin(Person):
    def add_room(self, room_detail: Room):
        pass

    def delete_room(self, room_id: str) -> Room:
        pass

    def edit_room(self, room_detail: Room):
        pass


class Search:
    def search_room(self, room_style: RoomStyle, start_date: date, duration: int) -> List[Room]:
        pass


class RoomBooking:
    def __init__(self, booking_id: str, start_date: date, duration_in_days: int,
                 booking_status: 'BookingStatus', guest_list: List[Guest],
                 room_info: List[Room], total_room_charges: 'BaseRoomCharge'):
        self.booking_id = booking_id
        self.start_date = start_date
        self.duration_in_days = duration_in_days
        self.booking_status = booking_status
        self.guest_list = guest_list
        self.room_info = room_info
        self.total_room_charges = total_room_charges


class BookingStatus(Enum):
    PENDING = 1
    CONFIRMED = 2
    CANCELLED = 3
    COMPLETED = 4


# Decorator pattern

class BaseRoomCharge(ABC):
    @abstractmethod
    def get_cost(self) -> float:
        pass


class RoomCharge(BaseRoomCharge):
    def __init__(self, cost: float):
        self.cost = cost

    def get_cost(self) -> float:
        return self.cost


class RoomServiceCharge(BaseRoomCharge):
    def __init__(self, base_room_charge: BaseRoomCharge, cost: float):
        self.base_room_charge = base_room_charge
        self.cost = cost

    def get_cost(self) -> float:
        return self.base_room_charge.get_cost() + self.cost


class InRoomPurchaseCharges(BaseRoomCharge):
    def __init__(self, base_room_charge: BaseRoomCharge, cost: float):
        self.base_room_charge = base_room_charge
        self.cost = cost

    def get_cost(self) -> float:
        return self.base_room_charge.get_cost() + self.cost


class Booking:
    def create_booking(self, guest_info: Guest) -> RoomBooking:
        pass

    def cancel_booking(self, booking_id: int) -> RoomBooking:
        pass
