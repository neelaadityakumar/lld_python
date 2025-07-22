from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Optional


class Color(Enum):
    BLACK = "BLACK"
    WHITE = "WHITE"


class GameStatus(Enum):
    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"
    FORFEIT = "FORFEIT"
    BLACK_WIN = "BLACK_WIN"
    WHITE_WIN = "WHITE_WIN"


class Time:
    def __init__(self, mins: int, secs: int):
        self.mins = mins
        self.secs = secs


class Account:
    def __init__(self, username: str, password: str, name: str, email: str, phone: str):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.phone = phone


class Player:
    def __init__(self, account: Account, color: Color, time_left: Time):
        self.account = account
        self.color = color
        self.time_left = time_left


class CellPosition:
    def __init__(self, ch: str, i: int):
        self.ch = ch
        self.i = i


class Cell:
    def __init__(self, color: Color, position: CellPosition, piece: Optional['Piece'] = None):
        self.color = color
        self.position = position
        self.piece = piece


class Move:
    def __init__(self, turn: Player, piece: 'Piece', start_position: CellPosition, end_position: CellPosition, killed_piece: Optional['Piece'] = None):
        self.turn = turn
        self.piece = piece
        self.start_position = start_position
        self.end_position = end_position
        self.killed_piece = killed_piece


class ChessBoard:
    def __init__(self):
        self.board: List[List[Cell]] = []

    def reset_board(self):
        pass


    def get_cell(self, position: CellPosition) -> Cell:
        row = position.i
        col = ord(position.ch.lower()) - ord('a')
        return self.board[row][col]

    def update_board(self, move: Move):
        from_cell = self.get_cell(move.start_position)
        to_cell = self.get_cell(move.end_position)

        to_cell.piece = move.piece
        from_cell.piece = None


class Piece(ABC):
    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def move(self, from_position: CellPosition, to_position: CellPosition) -> bool:
        pass

    @abstractmethod
    def possible_moves(self, from_position: CellPosition) -> List[CellPosition]:
        pass

    @abstractmethod
    def validate(self, from_position: CellPosition, to_position: CellPosition) -> bool:
        pass


# Derived Piece Classes

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
    def move(self, from_position, to_position):
        return True

    def possible_moves(self, from_position):
        return []

    def validate(self, from_position, to_position):
        return True


class Rook(Piece):
    def move(self, from_position, to_position):
        return True

    def possible_moves(self, from_position):
        return []

    def validate(self, from_position, to_position):
        return True


class Queen(Piece):
    def move(self, from_position, to_position):
        return True

    def possible_moves(self, from_position):
        return []

    def validate(self, from_position, to_position):
        return True


class King(Piece):
    def move(self, from_position, to_position):
        return True

    def possible_moves(self, from_position):
        return []

    def validate(self, from_position, to_position):
        return True


class Pawn(Piece):
    def move(self, from_position, to_position):
        return True

    def possible_moves(self, from_position):
        return []

    def validate(self, from_position, to_position):
        return True


class Chess:
    def __init__(self):
        self.chess_board = ChessBoard()
        self.players: List[Player] = []
        self.current_player: Optional[Player] = None
        self.moves_list: List[Move] = []
        self.game_status: GameStatus = GameStatus.ACTIVE

    def player_move(self, from_position: CellPosition, to_position: CellPosition, piece: Piece) -> bool:
        return True

    def end_game(self) -> bool:
        return True

    def _change_turn(self):
        if self.players:
            self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]
