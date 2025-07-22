from typing import List, Optional
from datetime import date
from enum import Enum


class Library:
    def __init__(self, name: str, location: 'Address'):
        self.name = name
        self.location = location
        self.books: List['BookItem'] = []

class Address:
    def __init__(self, pin_code: int, street: str, city: str, state: str, country: str):
        self.pin_code = pin_code
        self.street = street
        self.city = city
        self.state = state
        self.country = country


class Book:
    def __init__(self, unique_id_number: str, title: str, authors: List['Author'], book_type: 'BookType'):
        self.unique_id_number = unique_id_number
        self.title = title
        self.authors = authors
        self.book_type = book_type


class BookItem(Book):
    def __init__(
        self,
        unique_id_number: str,
        title: str,
        authors: List['Author'],
        book_type: 'BookType',
        barcode: str,
        publication_date: date,
        rack_location: 'Rack',
        book_status: 'BookStatus',
        book_format: 'BookFormat',
        issue_date: Optional[date] = None
    ):
        super().__init__(unique_id_number, title, authors, book_type)
        self.barcode = barcode
        self.publication_date = publication_date
        self.rack_location = rack_location
        self.book_status = book_status
        self.book_format = book_format
        self.issue_date = issue_date



class BookType(Enum):
    SCI_FI = "SCI_FI"
    ROMANTIC = "ROMANTIC"
    FANTASY = "FANTASY"
    DRAMA = "DRAMA"


class BookFormat(Enum):
    HARDCOVER = "HARDCOVER"
    PAPERBACK = "PAPERBACK"
    NEWSPAPER = "NEWSPAPER"
    JOURNAL = "JOURNAL"


class BookStatus(Enum):
    ISSUED = "ISSUED"
    AVAILABLE = "AVAILABLE"
    RESERVED = "RESERVED"
    LOST = "LOST"


class Rack:
    def __init__(self, number: int, location_id: str):
        self.number = number
        self.location_id = location_id


class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class Account:
    def __init__(self, username: str, password: str, account_id: int):
        self.username = username
        self.password = password
        self.account_id = account_id

class Author(Person):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.books_published: List[Book] = []


class SystemUser(Person):
    def __init__(self, first_name: str, last_name: str, email: str, phone_number: str, account: 'Account'):
        super().__init__(first_name, last_name)
        self.email = email
        self.phone_number = phone_number
        self.account = account


class Member(SystemUser):
    def __init__(self, first_name, last_name, email, phone, account):
        super().__init__(first_name, last_name, email, phone, account)
        self.total_book_checked_out: int = 0
        self.search_obj = Search()
        self.issue_service = BookIssueService()


class Librarian(SystemUser):
    def __init__(self, first_name, last_name, email, phone, account):
        super().__init__(first_name, last_name, email, phone, account)
        self.search_obj = Search()
        self.issue_service = BookIssueService()

    def add_book_item(self, book_item: BookItem):
        pass  # Implementation later

    def delete_book_item(self, barcode: str) -> Optional[BookItem]:
        pass

    def edit_book_item(self, book_item: BookItem) -> Optional[BookItem]:
        pass



class Search:
    def get_book_by_title(self, title: str) -> List[BookItem]:
        return []

    def get_book_by_author(self, author: Author) -> List[BookItem]:
        return []

    def get_book_by_type(self, book_type: BookType) -> List[BookItem]:
        return []

    def get_book_by_publication_date(self, publication_date: date) -> List[BookItem]:
        return []


class BookIssueService:
    def __init__(self):
        self.fine = Fine

    def get_reservation_detail(self, book: BookItem) -> Optional['BookReservationDetail']:
        return None

    def update_reservation_detail(self, book_reservation_detail: 'BookReservationDetail'):
        pass

    def reserve_book(self, book: BookItem, user: SystemUser) -> 'BookReservationDetail':
        return BookReservationDetail(book, date.today(), user, ReservationStatus.RESERVED)

    def issue_book(self, book: BookItem, user: SystemUser) -> 'BookIssueDetail':
        return BookIssueDetail(book, date.today(), user, date.today())

    def renew_book(self, book: BookItem, user: SystemUser) -> 'BookIssueDetail':
        return self.issue_book(book, user)

    def return_book(self, book: BookItem, user: SystemUser):
        pass


class BookLending:
    def __init__(self, book: BookItem, start_date: date, user: SystemUser):
        self.book = book
        self.start_date = start_date
        self.user = user


class BookReservationDetail(BookLending):
    def __init__(self, book: BookItem, start_date: date, user: SystemUser, reservation_status: 'ReservationStatus'):
        super().__init__(book, start_date, user)
        self.reservation_status = reservation_status


class BookIssueDetail(BookLending):
    def __init__(self, book: BookItem, start_date: date, user: SystemUser, due_date: date):
        super().__init__(book, start_date, user)
        self.due_date = due_date


class Fine:
    def __init__(self, fine_date: date, book: BookItem, user: SystemUser):
        self.fine_date = fine_date
        self.book = book
        self.user = user

    def calculate_fine(self, days: int) -> float:
        return days * 10.0  # Example rate: ₹10 per day


class ReservationStatus(Enum):
    RESERVED = "RESERVED"
    WAITING = "WAITING"
    CANCELED = "CANCELED"
