# Telegram bot for providing information from Google Sheets (aiogram, pygsheets)

![Иллюстрация к проекту](https://github.com/PavelShaura/GooglesheetAPI_bot_aiogram_3.0.0/blob/master/images/chat.png)

![Иллюстрация к проекту](https://github.com/PavelShaura/GooglesheetAPI_bot_aiogram_3.0.0/blob/master/images/sheet_examle.png)

## Installation
1. Install Python 3.x if it is not installed. [Python.org](https://www.python.org/downloads/)

2. Clone the repository:

   ```bash
   git clone https://github.com/PavelShaura/GooglesheetAPI_bot_aiogram_3.0.0
   
3. Navigate to the project catalog:

   ```bash
   cd GooglesheetAPI_bot_aiogram_3.0.0
   
4. Install the dependencies using pip:

   ```bash
   pip install -r requirements.txt
   
## Configuration

Create an .env configuration file in the root directory of the project and specify the following environment variables:

* TELEGRAM_TOKEN=
* LOG_FILE_PATH=log_file.ini (You can leave it like this. It will be created automatically in the project root when the bot is launched for the first time).
* DOC_URL=


YOUR_TELEGRAM_BOT_TOKEN - Your Telegram bot token. Get it from BotFather.

log_file.ini- The name of the .ini file for storing logs.

YOUR_GOOGLE_SHEET_URL - The URL of your Google spreadsheet to access your subscription data.

Please remember to replace `TELEGRAM_TOKEN` and your `DOC_URL` with real values, and make sure you have a `credentials_API.json` file to access the Google Sheets API.

How to allow access and download your credetials.json [here]([https://support.google.com/a/answer/7378726?hl=ru](https://developers.google.com/sheets/api/quickstart/go?hl=ru)


<div id="header">
  <img src="https://media.giphy.com/media/3b6rWgdpjf0jrvvvZ6/giphy.gif" width="100"/>
</div>

Questions and suggestions: https://t.me/PavelShau

## Start

Start the bot, run the following command in the root directory of the project:

   ```bash 
   python bot.py

