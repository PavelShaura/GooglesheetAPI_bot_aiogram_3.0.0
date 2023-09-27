LEXICON_RU: dict[str, str] = {
    "/start": "🤖 КОМАНДЫ ДЛЯ ЧАТ-БОТА: 🤖\n\n"
    "❗ /check ❗\n"
    f"-- Информация о Вашем абонементе (дата окончания и количество оставшихся занятий) 🔖\n\n"
    "❗ /location ❗\n"
    "-- наш адрес, карта и инструкция, как нас найти 🗺\n\n"
    "❗ /price ❗\n"
    "-- цены на занятия и программа лояльности 💰\n\n"
    "❗ /worktime ❗\n"
    "-- расписание занятий 📆\n\n"
    "Если у Вас иной вопрос, то напишите и вам ответит администратор 👤 @GcontentPavel",
    "/check": "Напишите ID своего абонемента чтобы узнать количество оставшихся занятий\n\n"
    "Для отмены отправьте команду /cancel",
    "/cancel_empty": "Отменять нечего.\n\n"
    "Чтобы знать количество оставшихся занятий - "
    "отправьте команду /check",
    "/cancel_on": "Вы отменили ввод данных\n\n"
    "Чтобы знать количество оставшихся занятий - "
    "отправьте команду /check",
    "error_user": "Такого абонемента не существует, либо его срок действия закончился 😰",
}

LEXICON_COMMANDS_RU: dict[str, str] = {
    "/start": "Старт бота  и описание доступных комманд",
    "/check": "Проверка статуса абонемента",
    "/price": "Узнать цены",
    "/worktime": "Расписание",
    "/location": "Как добраться",
}
