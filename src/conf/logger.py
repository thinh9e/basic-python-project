from dataclasses import dataclass

from src.enums.logger import LoggerLevel


@dataclass
class LoggerConfig:
    """Logger config"""

    folder: str
    file: str
    level: LoggerLevel
    backup: int

    def __post_init__(self) -> None:
        if self.level not in list(LoggerLevel):
            print(f"Error: {self.level} is not a valid value")
            print("-> logger.level:", list(map(str, LoggerLevel)))
            exit(1)
