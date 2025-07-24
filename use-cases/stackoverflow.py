from typing import List, Dict
from datetime import date
from enum import Enum


class User:
    def __init__(self, guest_id: int):
        self.guest_id = guest_id
        self.search_obj = None

    def get_questions(self, search_string: str) -> List["Question"]:
        pass


class Member(User):
    def __init__(self, guest_id: int, account: "Account"):
        super().__init__(guest_id)
        self.account = account
        self.badges: List[Badge] = []

    def add_question(self, question: "Question"):
        pass

    def add_comment(self, entity: "Entity", comment: "Comment"):
        pass

    def add_answer(self, question: "Question", answer: "Answer"):
        pass

    def vote(self, entity: "Entity", vote_type: "VoteType"):
        pass

    def add_tag(self, question: "Question", tag: "Tag"):
        pass

    def flag(self, entity: "Entity"):
        pass

    def get_badges(self) -> List["Badge"]:
        return self.badges


class Account:
    def __init__(self, name: str, address: "Address", account_id: int,
                 user_name: str, password: str, email: str,
                 account_status: "AccountStatus", reputation: int):
        self.name = name
        self.address = address
        self.account_id = account_id
        self.user_name = user_name
        self.password = password
        self.email = email
        self.account_status = account_status
        self.reputation = reputation


class Moderator(Member):
    def close_question(self, question: "Question") -> bool:
        pass

    def restore_question(self, question: "Question") -> bool:
        pass


class Admin(Member):
    def block_member(self, member: Member) -> bool:
        pass

    def unblock_member(self, member: Member) -> bool:
        pass


class AccountStatus(Enum):
    BLOCKED = "BLOCKED"
    ACTIVE = "ACTIVE"
    CLOSED = "CLOSED"


class VoteType(Enum):
    UPVOTE = "UPVOTE"
    DOWNVOTE = "DOWNVOTE"
    CLOSEVOTE = "CLOSEVOTE"
    DELETEVOTE = "DELETEVOTE"


class Badge:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description


class Entity:
    def __init__(self, entity_id: int, creator: Member, created_date: date):
        self.entity_id = entity_id
        self.creator = creator
        self.votes: Dict[VoteType, int] = {}
        self.created_date = created_date
        self.comments: List[Comment] = []

    def flag_entity(self, member: Member) -> bool:
        pass

    def vote_entity(self, vote_type: VoteType) -> bool:
        pass

    def add_comment(self, comment: "Comment") -> bool:
        pass


class Comment(Entity):
    def __init__(self, entity_id: int, creator: Member, created_date: date, message: str):
        super().__init__(entity_id, creator, created_date)
        self.message = message


class Question(Entity):
    def __init__(self, entity_id: int, creator: Member, created_date: date,
                 title: str, description: str, status: "QuestionStatus"):
        super().__init__(entity_id, creator, created_date)
        self.edit_history_list: List[EditHistory] = []
        self.answer_list: List[Answer] = []
        self.tags: List[Tag] = []
        self.title = title
        self.description = description
        self.status = status

    def add_question(self) -> bool:
        pass

    def add_tag(self, tag: "Tag") -> bool:
        pass


class Answer(Entity):
    def __init__(self, entity_id: int, creator: Member, created_date: date,
                 answer: str, is_accepted: bool):
        super().__init__(entity_id, creator, created_date)
        self.answer = answer
        self.is_accepted = is_accepted

    def add_answer(self, question: Question) -> bool:
        pass


class QuestionStatus(Enum):
    ACTIVE = "ACTIVE"
    BOUNTIED = "BOUNTIED"
    CLOSED = "CLOSED"
    FLAGGED = "FLAGGED"


class Tag:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description


class EditHistory:
    def __init__(self, edit_history_id: int, creator: Member,
                 creation_date: date, prev_question: Question, updated_question: Question):
        self.edit_history_id = edit_history_id
        self.creator = creator
        self.creation_date = creation_date
        self.prev_question = prev_question
        self.updated_question = updated_question


class Address:
    def __init__(self, street: str, city: str, state: str, country: str, pin_code: str):
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.pin_code = pin_code
