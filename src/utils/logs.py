import logging
import logging.handlers
from pathlib import Path

from src.utils.configs import Config
from src.utils.constants import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class _LogHandler:
    """
    Define log handler
    """

    def __init__(self) -> None:
        fmt = "%(asctime)s [%(levelname)s] %(message)s"
        date_fmt = "%Y-%m-%d %H:%M:%S"
        self._formatter = logging.Formatter(fmt=fmt, datefmt=date_fmt)

    def file_handler(self) -> logging.Handler:
        """
        Log to file

        :return: File handler
        """
        log_dir = Config.logger().folder
        Path(log_dir).mkdir(parents=True, exist_ok=True)

        filename = f"{log_dir}/{Config.logger().file}"
        handler = logging.handlers.TimedRotatingFileHandler(
            filename=filename, when="MIDNIGHT", backupCount=Config.logger().backup
        )
        handler.suffix = "%Y%m%d"
        handler.setFormatter(self._formatter)
        return handler

    def stream_handler(self) -> logging.Handler:
        """
        Log to console

        :return: Stream handler
        """
        handler = logging.StreamHandler()
        handler.setFormatter(self._formatter)
        return handler


def init_logger() -> None:
    """
    Initialize logger

    :return: None
    """
    logger.setLevel(Config.logger().level)

    handler = _LogHandler()
    logger.addHandler(handler.file_handler())
    logger.addHandler(handler.stream_handler())
