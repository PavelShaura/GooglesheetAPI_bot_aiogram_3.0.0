from lexicon.lexicon_ru import LEXICON_RU


def construct_answer(values: list):
    """
    Функция для формирования ответа пользователю на основе данных из таблицы.
    Args:
        values: Значения, полученные из таблицы (list).
    Returns
        str: Сообщение для пользователя, содержащее информацию о сроке действия абонемента,
        и остатке занятий.
    """
    if values == -1:
        user_message = LEXICON_RU["error_user"]
    else:
        end_date_value = values[0]
        balance_value = int(values[1])
        last_digit = balance_value % 10

        if last_digit == 1 and balance_value != 11:
            balance_value = f"{balance_value} занятие"
        elif last_digit in (2, 3, 4) and balance_value not in (12, 13, 14):
            balance_value = f"{balance_value} занятия"
        else:
            balance_value = f"{balance_value} занятий"
        user_message = (
            f"🗓 Ваш абонемент заканчивается {end_date_value}\n💃 "
            f"У Вас осталось {balance_value}"
        )
    return user_message
