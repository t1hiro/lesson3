import logging
from datetime import datetime

import ephem
import copy
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from settings import API_KEY, PROXY

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
CITIES_CHATS = {}

def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)

def get_planet(bot, update):
    text = update.message.text.split()
    logging.info(text)
    try:
        if len(text) == 1:
            update.message.reply_text('Введите значение после команды /planet')
        planet = getattr(ephem, text[1])(datetime.now().strftime('%Y/%m/%d/'))
        _, constellation_name = ephem.constellation(planet)
        update.message.reply_text(constellation_name)
    except AttributeError:
        update.message.reply_text('Такой планеты не существует')

def get_wordcount(bot, update):
    text = update.message.text.split()[1:]
    if text:
        while '' in text:
            text.remove('')
        logging.info(text)
        update.message.reply_text('{} слова'.format(len(text)))
    else:
        update.message.reply_text('Введите значение после команды')

def get_next_full_moon(bot, update):
    text = update.message.text.split()
    logging.info(text)
    if len(text) > 1:
        try:
            date = datetime.strptime(text[1], '%Y-%m-%d')
            update.message.reply_text(ephem.next_full_moon(date.strftime('%Y/%m/%d/')))
        except ValueError:
            update.message.reply_text('Введите дату в формате ГГГГ-ММ-ДД')    
    else:
        update.message.reply_text(ephem.next_full_moon(datetime.now().strftime('%Y/%m/%d/')))

def cities_game(bot, update):
    cities_list = ['Москва', 'Абакан', 'Новосибирск', 'Курск', 'Калиниград', 'Донецк', 'Киев', 'Владимир']
    text = update.message.text.split()
    if str(update.message.chat.id) not in CITIES_CHATS:
        CITIES_CHATS[str(update.message.chat.id)] = cities_list
    logging.info(text)
    if len(text) > 1:
        cities_list_ = CITIES_CHATS[str(update.message.chat.id)]
        if text[1] in cities_list_:
            cities_list_.remove(text[1]) 
            city = cities_list_[[word[0].lower() for word in cities_list_].index(text[1][-1])]
            cities_list_.remove(city) 
            update.message.reply_text(city)
        else:
            update.message.reply_text('Такого города нет в списке доступных \n введите один из {}'.format(', '.join(cities_list_)))
    elif text[0] == '/cities_new' and str(update.message.chat.id) in CITIES_CHATS:
        del CITIES_CHATS[str(update.message.chat.id)]        
    else:
        update.message.reply_text('Введите город')


def talk_to_me(bot, update):
    user_text = "Привет, {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.username, 
    	update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(API_KEY, request_kwargs=PROXY)

    logging.info('Бот запускается')
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', get_planet))
    dp.add_handler(CommandHandler('wordcount', get_wordcount))
    dp.add_handler(CommandHandler('next_full_moon', get_next_full_moon))
    dp.add_handler(CommandHandler('cities', cities_game))
    dp.add_handler(CommandHandler('cities_new', cities_game))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()