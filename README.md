# Telegram бот для предоставления информации о пользовательских абонементах зааписаных в Google Sheets

![Иллюстрация к проекту]https://github.com/PavelShaura/GooglesheetAPI_bot_aiogram_3.0.0/blob/master/images/chat.png
## Установка (aiogram, pygsheets)
1. Установите Python 3.x, если он не установлен. [Python.org](https://www.python.org/downloads/)

2. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/PavelShaura/GooglesheetAPI_bot_aiogram_3.0.0
   
3. Перейдите в каталог проекта:

   ```bash
   cd GooglesheetAPI_bot_aiogram_3.0.0
   
4. Установите зависимости, используя pip:

   ```bash
   pip install -r requirements.txt
   
## Настройка

Создайте файл конфигурации .env в корневом каталоге проекта и укажите следующие переменные окружения:

* TELEGRAM_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
* LOG_FILE_PATH=logs/bot.log
* DOC_URL=YOUR_GOOGLE_SHEET_URL


YOUR_TELEGRAM_BOT_TOKEN - Токен вашего Telegram бота. Получите его у BotFather.

logs/bot.log - Файл для хранения логов. Создается автоматически в корне проекта при первом запуске бота.

YOUR_GOOGLE_SHEET_URL - URL вашей Google таблицы для доступа к данным абонементов.

Пожалуйста, не забудьте заменить `YOUR_TELEGRAM_BOT_TOKEN` и `YOUR_GOOGLE_SHEET_URL` на реальные значения, а также убедитесь, что у вас есть файл `credentials_API.json` для доступа к Google Sheets API.

Как разрешить доступ и скачать свой credetials.json [сдесь](https://support.google.com/a/answer/7378726?hl=ru)

## Запуск

Запустите бота, выполните следующую команду в корневом каталоге проекта:

   ```bash 
   python bot.py
