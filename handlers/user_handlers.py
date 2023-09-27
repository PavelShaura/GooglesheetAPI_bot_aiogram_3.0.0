from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

from bot import main
from lexicon.lexicon_ru import LEXICON_RU

from services.utils import construct_answer

from loguru import logger


# Создание роутера и хранилища состояний
router = Router()
storage = MemoryStorage()


# Определение состояния для FSM (Finite State Machine)
class CheckState(StatesGroup):
    waiting_for_abonement_id = State()


# Обработчик для команды /check
@router.message(Command(commands="check"), StateFilter(default_state))
async def start_abonement_check(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_RU["/check"])
    await state.set_state(CheckState.waiting_for_abonement_id)


# Обработчик команды /cancel в начальном состоянии
@router.message(Command(commands="cancel"), StateFilter(default_state))
async def process_cancel_command(message: Message):
    await message.answer(text=LEXICON_RU["/cancel_empty"])


# Обработчик команды /cancel в состоянии ожидания ID абонемента
@router.message(Command(commands="cancel"), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_RU["/cancel_on"])
    await state.clear()


@router.message(StateFilter(CheckState.waiting_for_abonement_id), F.text.isdigit())
async def process_abonement_id(message: Message, state: FSMContext, bot: main):
    """
    Обработчик ID абонемента и запроса количества оставшихся занятий.
    Args:
        message (Message): Сообщение от пользователя.
        state (FSMContext): Контекст FSM для управления состоянием.
        bot (main): Экземпляр основного модуля бота.
    Returns:
        None
    """
    user_id: str = str(message.from_user)
    abonement_id = message.text
    values = bot.google_table.search_abonement(abonement_id)
    values_result = construct_answer(values)
    try:
        await message.answer(values_result)
    except Exception as error:
        logger.debug(f"{error}: Trouble id: {user_id}")
        return
    await state.clear()
