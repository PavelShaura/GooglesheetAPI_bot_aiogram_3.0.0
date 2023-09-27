from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import FSInputFile

from loguru import logger


router = Router()


# Обработчик команды /price
@router.message(Command(commands="price"))
async def prices_handler(message: types.Message) -> None:
    user_id: str = str(message.from_user)
    price_photo = FSInputFile("images/price.png")
    try:
        await message.answer_photo(photo=price_photo)
    except Exception as error:
        logger.debug(f"{error}: Trouble id: {user_id}")
        return


# Обработчик команды /worktime
@router.message(Command(commands="worktime"))
async def worktime_handler(message: types.Message) -> None:
    user_id: str = str(message.from_user)
    worktime_photo = FSInputFile("images/worktime.png")
    try:
        await message.answer_photo(photo=worktime_photo)
    except Exception as error:
        logger.debug(f"{error}: Trouble id: {user_id}")
        return


# Обработчик команды /location
@router.message(Command(commands="location"))
async def how_to_get_handler(message: types.Message) -> None:
    user_id: str = str(message.from_user)
    location_photo = FSInputFile("images/location.jpg")
    try:
        await message.answer_photo(photo=location_photo)
    except Exception as error:
        logger.debug(f"{error}: Trouble id: {user_id}")
        return
