from aiogram import Bot
from googleAPI.googlesheet_table import GoogleTable


class TelegramBot(Bot):
    def __init__(
        self,
        token: str,
        parse_mode,
        google_table: GoogleTable = None,
    ) -> None:
        """
        Конструктор класса TelegramBot.
        Args:
            token (str): Токен бота, используемый для взаимодействия с Telegram API.
            parse_mode: Режим парсинга сообщений (HTML, Markdown или None).
            google_table (GoogleTable, optional): Объект GoogleTable для работы с Google Sheets.
            По умолчанию None.
        Returns:
            None
        """
        # Вызываем конструктор базового класса Bot
        super().__init__(token, parse_mode=parse_mode)
        # Инициализируем атрибут _google_table объектом GoogleTable или None, если он не передан
        self.google_table: GoogleTable = google_table
