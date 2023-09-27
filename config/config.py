from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    log_file: str
    doc_url: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    """
    Загружает конфигурацию из файла окружения и создает объект Config.
    Args:
        path (str, optional): Путь к файлу окружения.
        Если не указан, будет использован файл .env по умолчанию.
    Returns:
        Config: Объект конфигурации, содержащий настройки бота и другие параметры.
    """
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env("TELEGRAM_TOKEN"),
            log_file=env("LOG_FILE_PATH"),
            doc_url=env("DOC_URL"),
        )
    )
