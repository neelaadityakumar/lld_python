from typing import List, Dict
from datetime import date, datetime
from enum import Enum


class BMSService:
    def __init__(self):
        self.cinemas: List[CinemaHall] = []

    def get_movies(self, date: date, city: str) -> List['Movie']:
        pass

    def get_cinemal_halls(self, city: str) -> List['CinemaHall']:
        pass


class CinemaHall:
    def __init__(self):
        self.cinema_hall_id: int = 0
        self.cinema_hall_name: str = ""
        self.address: Address = None
        self.audi_list: List['Audi'] = []

    def get_movies(self, date_list: List[date]) -> Dict[date, 'Movie']:
        pass

    def get_shows(self, date_list: List[date]) -> Dict[date, 'Show']:
        pass


class Address:
    def __init__(self):
        self.pin_code: int = 0
        self.street: str = ""
        self.city: str = ""
        self.state: str = ""
        self.country: str = ""


class Audi:
    def __init__(self):
        self.audi_id: int = 0
        self.audi_name: str = ""
        self.total_seats: int = 0
        self.shows: List['Show'] = []


class Show:
    def __init__(self):
        self.show_id: int = 0
        self.movie: 'Movie' = None
        self.start_time: datetime = None
        self.end_time: datetime = None
        self.cinema_played_at: 'CinemaHall' = None
        self.seats: List['Seat'] = []


class Seat:
    def __init__(self):
        self.seat_id: int = 0
        self.seat_type: 'SeatType' = None
        self.seat_status: 'SeatStatus' = None
        self.price: float = 0.0


class SeatType(Enum):
    DELUX = 1
    VIP = 2
    ECONOMY = 3
    OTHER = 4


class SeatStatus(Enum):
    BOOKED = 1
    AVAILABLE = 2
    RESERVED = 3
    NOT_AVAILABLE = 4


class Movie:
    def __init__(self):
        self.movie_name: str = ""
        self.movie_id: int = 0
        self.duration_in_mins: int = 0
        self.language: str = ""
        self.genre: 'Genre' = None
        self.release_date: date = None
        self.city_show_map: Dict[str, List['Show']] = {}


class Genre(Enum):
    SCI_FI = 1
    DRAMA = 2
    ROM_COM = 3
    FANTASY = 4


class User:
    def __init__(self):
        self.user_id: int = 0
        self.search_obj: 'Search' = None


class SystemMember(User):
    def __init__(self):
        super().__init__()
        self.account: 'Account' = None
        self.name: str = ""
        self.email: str = ""
        self.address: 'Address' = None


class Member(SystemMember):
    def make_booking(self, booking: 'Booking') -> 'Booking':
        pass

    def get_booking(self) -> List['Booking']:
        pass


class Admin(SystemMember):
    def add_movie(self, movie: 'Movie') -> bool:
        pass

    def add_show(self, show: 'Show') -> bool:
        pass


class Account:
    def __init__(self):
        self.user_name: str = ""
        self.password: str = ""


class Search:
    def search_movies_by_names(self, name: str) -> List['Movie']:
        pass

    def search_movies_by_genre(self, genre: 'Genre') -> List['Movie']:
        pass

    def search_movies_by_language(self, language: str) -> List['Movie']:
        pass

    def search_movies_by_date(self, release_date: date) -> List['Movie']:
        pass


class Booking:
    def __init__(self):
        self.booking_id: str = ""
        self.booking_date: date = None
        self.member: 'Member' = None
        self.audi: 'Audi' = None
        self.show: 'Show' = None
        self.booking_status: 'BookingStatus' = None
        self.total_amount: float = 0.0
        self.seats: List['Seat'] = []
        self.payment_obj: 'Payment' = None

    def make_payment(self, payment: 'Payment') -> bool:
        pass


class Payment:
    def __init__(self):
        self.amount: float = 0.0
        self.payment_date: date = None
        self.transaction_id: int = 0
        self.payment_status: 'PaymentStatus' = None


class BookingStatus(Enum):
    REQUESTED = 1
    PENDING = 2
    CONFIRMED = 3
    CANCELLED = 4


class PaymentStatus(Enum):
    UNPAID = 1
    PENDING = 2
    COMPLETED = 3
    DECLINED = 4
    CANCELLED = 5
    REFUNDED = 6
