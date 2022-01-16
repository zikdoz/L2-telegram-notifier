from telebot import *

import logging
import os

def configLogger():
    main_logger = logging.getLogger()
    
    custom_formatter = logging.Formatter(fmt='[{asctime}] [ {levelname:^10s}] `{module}`: {message}', style='{')

    os.makedirs(name='./logs/', exist_ok=True)

    file_handler = logging.FileHandler(filename='./logs/bot.log', mode='w', encoding='utf-8')
    file_handler.setFormatter(custom_formatter)
    main_logger.addHandler(file_handler)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(custom_formatter)
    main_logger.addHandler(console_handler)

    main_logger.setLevel(logging.NOTSET)

def main():
    configLogger()

    logging.info('firing up telegram bot..')
    
    telebot = TeleBot()
    telebot.readConfig('tele-config.yaml')

if __name__ == '__main__':
    main()