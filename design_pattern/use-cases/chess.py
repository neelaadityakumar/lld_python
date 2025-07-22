
from typing import List, Optional
from enum import Enum
from abc import ABC, abstractmethod


class Chess:
    def __init__(self):
        self.chess_board: ChessBoard = ChessBoard()
        self.player: List[Player] = []
        self.current_player: Optional[Player] = None
        self.moves_list: List[Move] = []
        self.game_status: Optional[GameStatus] = None

    def player_move(self, from_position: 'CellPosition', to_position: 'CellPosition', piece: 'Piece') -> bool:
        pass

    def end_game(self) -> bool:
        pass

    def __change_turn(self):
        pass


class Player:
    def __init__(self):
        self.account: Account = Account()
        self.color: Optional[Color] = None
        self.time_left: Time = Time()


class Time:
    def __init__(self):
        self.mins: int = 0
        self.secs: int = 0


class Color(Enum):
    BLACK = 1
    WHITE = 2


class Account:
    def __init__(self):
        self.username: str = ""
        self.password: str = ""
        self.name: str = ""
        self.email: str = ""
        self.phone: str = ""


class GameStatus(Enum):
    ACTIVE = 1
    PAUSED = 2
    FORTFEIGHT = 3
    BLACK_WIN = 4
    WHITE_WIN = 5


class ChessBoard:
    def __init__(self):
        self.board: List[List['Cell']] = []

    def reset_board(self):
        pass

    def update_board(self, move: 'Move'):
        pass


class Cell:
    def __init__(self):
        self.color: Optional[Color] = None
        self.piece: Optional[Piece] = None
        self.position: Optional['CellPosition'] = None


class CellPosition:
    def __init__(self):
        self.ch: str = ''
        self.i: int = 0


class Move:
    def __init__(self):
        self.turn: Optional[Player] = None
        self.piece: Optional[Piece] = None
        self.killed_piece: Optional[Piece] = None
        self.start_position: Optional[CellPosition] = None
        self.end_position: Optional[CellPosition] = None


class Piece(ABC):
    def __init__(self):
        self.color: Optional[Color] = None

    @abstractmethod
    def move(self, from_position: 'CellPosition', to_position: 'CellPosition') -> bool:
        pass

    @abstractmethod
    def possible_moves(self, from_position: 'CellPosition') -> List['CellPosition']:
        pass

    @abstractmethod
    def validate(self, from_position: 'CellPosition', to_position: 'CellPosition') -> bool:
        pass



class Knight(Piece):
    def move(self, from_position, to_position):
        return self.validate(from_position, to_position)

    def possible_moves(self, from_position):
        moves = []
        directions = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                      (-2, -1), (-1, -2), (1, -2), (2, -1)]

        for dx, dy in directions:
            col = ord(from_position.ch) - ord('a') + dx
            row = from_position.i + dy
            if 0 <= col < 8 and 0 <= row < 8:
                moves.append(CellPosition(chr(col + ord('a')), row))
        return moves

    def validate(self, from_position, to_position):
        dx = abs(ord(to_position.ch) - ord(from_position.ch))
        dy = abs(to_position.i - from_position.i)
        return (dx, dy) in [(1, 2), (2, 1)]



class Bishop(Piece):
    def move(self, from_position: 'CellPosition', to_position: 'CellPosition') -> bool:
        pass

    def possible_moves(self, from_position: 'CellPosition') -> List['CellPosition']:
        pass

    def validate(self, from_position: 'CellPosition', to_position: 'CellPosition') -> bool:
        pass


class Rook(Piece):
    def move(self, from_position: 'CellPosition', to_position: 'CellPosition') -> bool:
        pass

    def possible_moves(self, from_position: 'CellPosition') -> List['CellPosition']:
        pass

    def validate(self, from_position: 'CellPosition', to_position: 'CellPosition') -> bool:
        pass


class King(Piece):
    def move(self, from_position: 'CellPosition', to_position: 'CellPosition') -> bool:
        pass

    def possible_moves(self, from_position: 'CellPosition') -> List['CellPosition']:
        pass

    def validate(self, from_position: 'CellPosition', to_position: 'CellPosition') -> bool:
        pass


class Queen(Piece):
    def move(self, from_position: 'CellPosition', to_position: 'CellPosition') -> bool:
        pass

    def possible_moves(self, from_position: 'CellPosition') -> List['CellPosition']:
        pass

    def validate(self, from_position: 'CellPosition', to_position: 'CellPosition') -> bool:
        pass


class Pawn(Piece):
    def move(self, from_position: 'CellPosition', to_position: 'CellPosition') -> bool:
        pass

    def possible_moves(self, from_position: 'CellPosition') -> List['CellPosition']:
        pass

    def validate(self, from_position: 'CellPosition', to_position: 'CellPosition') -> bool:
        pass

