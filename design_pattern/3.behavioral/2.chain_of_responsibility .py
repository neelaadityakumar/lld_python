
from abc import ABC, abstractmethod

class LogLevel:
    DEBUG,INFO ,ERROR = 1,2,3

class Logger(ABC):
    def __init__(self, level):
        self.level = level
        self.next_logger = None

    def set_next(self, next_logger):
        self.next_logger = next_logger
        return next_logger  # enable chaining

    def log(self, level, message):
        if self.level <= level:
            self._write(message)
        if self.next_logger:
            self.next_logger.log(level, message)

    @abstractmethod
    def _write(self, message):
        pass


class DebugLogger(Logger):
    def __init__(self):
        super().__init__(LogLevel.DEBUG)

    def _write(self, message):
        print(f"[DEBUG]: {message}")

class InfoLogger(Logger):
    def __init__(self):
        super().__init__(LogLevel.INFO)

    def _write(self, message):
        print(f"[INFO]: {message}")

class ErrorLogger(Logger):
    def __init__(self):
        super().__init__(LogLevel.ERROR)

    def _write(self, message):
        print(f"[ERROR]: {message}")

# Set up the chain
logger_chain = DebugLogger()
logger_chain.set_next(InfoLogger()).set_next(ErrorLogger())

# Send messages
logger_chain.log(LogLevel.DEBUG, "Debugging connection issue")
logger_chain.log(LogLevel.INFO, "User logged in")
logger_chain.log(LogLevel.ERROR, "Unable to connect to DB")

