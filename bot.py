from aiogram import Dispatcher

import asyncio

from loguru import logger

from config.config import Config, load_config
from googleAPI.googlesheet_table import GoogleTable
from services.bot_init import TelegramBot
from handlers import user_handlers, info_handlers, other_handlers
from menu.set_menu import set_main_menu


async def main():
    # Загрузка конфигурации из файла
    config: Config = load_config()

    # Настройка логирования
    logger.add(
        config.tg_bot.log_file,
        format="{time} {level} {message}",
        level="DEBUG",
        rotation="1 week",
        compression="zip",
    )
    logger.info("Bot starting")

    # Инициализация экземпляра класса TelegramBot с использованием конфигурации
    bot: TelegramBot = TelegramBot(
        token=config.tg_bot.token,
        parse_mode="HTML",
        google_table=GoogleTable("credentials_API.json", config.tg_bot.doc_url),
    )

    # Создание диспетчера для обработки сообщений и команд
    dp = Dispatcher()

    # Включение роутеров для обработки хендлеров
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)
    dp.include_router(info_handlers.router)

    # Очистка вебхука и настройка основного меню бота
    await bot.delete_webhook(drop_pending_updates=True)
    await set_main_menu(bot)

    # Запуск бота с использованием диспетчера для обработки сообщений
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
