from telebot import *

def main():
    telebot = TeleBot()
    telebot.readConfig('tele-config.yaml')

if __name__ == '__main__':
    main()