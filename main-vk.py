import vk_api
import pandas as pd
import os
from database import add_data
from dotenv import load_dotenv

load_dotenv()

# Авторизация в ВК
vk = vk_api.VkApi(token= os.environ['TG_key'])

bot = vk_api.Bot(vk, 'ваш_бот')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
    keyboard.add_button('Отправить свой Excel')
    bot.send_message(message.peer_id, 'Привет! Отправь мне свой Excel, чтобы я записал твои данные и вывел их', keyboard=keyboard)

# Обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def handle_contact(message):
    if message.text == 'Отправить свой Excel':
        os.system('explorer')

# Обработчик документов
@bot.message_handler(content_types=['document'])
def handle_excele(message):
    if message.document:
        file_id = message.document['id']
        file_name = message.document['title']
        if file_name.endswith('.xlsx') or file_name.endswith('.xls'):
            file_path = vk.method('docs.get', {'doc_id': file_id})['url']
            file = vk.method('docs.get', {'doc_id': file_id})['file']
            path = os.path.join(os.getcwd(),'static', file_name)                                                                                                                                                       
            with open(os.path.join(path), 'wb') as f:
                f.write(file)
            df = pd.read_excel(path)
            for index, row in df.iterrows():
                for column, value in row.items():
                    bot.send_message(message.peer_id, f"{column} {value}")
                title = row['title']
                url = row['url']
                xpath = row['xpath']
                add_data(title, url, xpath)
        else:
            bot.send_message(message.peer_id, 'Пожалуйста, отправьте Excel-файл (.xlsx или .xls)')

bot.polling(none_stop=True)
#это код для основного бота в вк,не дописан