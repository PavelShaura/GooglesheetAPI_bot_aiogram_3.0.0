from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU

from loguru import logger


router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    user_id: str = str(message.from_user)
    try:
        await message.answer(text=LEXICON_RU["/start"])
    except Exception as error:
        logger.debug(f"{error}: Trouble id: {user_id}")
        return
