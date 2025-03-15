
import pandas as pd
import telebot
import sys
from database import add_data
import os
from dotenv import load_dotenv
load_dotenv()
api = os.environ['TG_key']

bot = telebot.TeleBot(api)


@bot.message_handler(commands=['start'])
def handle_start(message):
    keyboard  = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(telebot.types.KeyboardButton(text='Отправить свой Excel'))
    # Отправляем приветственное сообщение с кнопкой
    bot.send_message(message.chat.id, 'Привет! Отправь мне свой Excel, чтобы я записал твои данные и вывел их', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def handle_contact(message):
    if message.text == 'Отправить свой Excel':
        os.system('explorer')
        # ни в какой официальной документации не прописано что можно присылать файлы через кнопку,также прошарив весь инет информации о реализации такого не нашел


@bot.message_handler(content_types=['document'])
def handle_excele(message):
        if message.document:
            file_id = message.document.file_id
            file_name = message.document.file_name
            if file_name.endswith('.xlsx') or file_name.endswith('.xls'):
                file_id = message.document.file_id
                file_name = message.document.file_name
                file_path = bot.get_file(file_id).file_path
                file = bot.download_file(file_path)
                path = os.path.join(os.getcwd(),'static', file_name)                                                                                                                                                       
                with open(os.path.join(path), 'wb') as f:
                    f.write(file)
                df = pd.read_excel(path)
                for index, row in df.iterrows():
                    for column, value in row.items():
                        bot.send_message(message.chat.id,f"{column} {value}")
                    title = row['title']
                    url = row['url']
                    xpath = row['xpath']
                    add_data(title, url, xpath)
            else:
                bot.send_message(message.chat.id, 'Пожалуйста, отправьте Excel-файл (.xlsx или .xls)')


bot.polling(none_stop=True)
#это код для основного бота в тг