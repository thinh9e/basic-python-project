import tomllib

from src.conf.logger import LoggerConfig
from src.utils.constants import CONFIG_FILE


class Config:
    """Configuration"""

    raw_config: dict

    @classmethod
    def logger(cls) -> LoggerConfig:
        return LoggerConfig(**cls.raw_config["logger"])


def init_config(config_file: str = CONFIG_FILE) -> None:
    """
    Load configuration from file

    :param config_file: Config file
    :return: None
    """
    try:
        with open(config_file, "rb") as f:
            Config.raw_config = tomllib.load(f)
    except OSError as exp:
        print("Failed to load file:", config_file, exp)
        exit(1)
