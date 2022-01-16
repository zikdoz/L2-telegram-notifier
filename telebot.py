import pathlib
import logging
import sys
import yaml

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

class TeleBot:
    _auth_token = ''

    def readConfig(self, config_path):
        logging.info(f'trying to parse given config: `{config_path}`')
        
        config_file = pathlib.Path(config_path)
        if not config_file.exists():
            logging.critical(f'given config path does not exist: `{config_path}`')
            sys.exit(42)

        config_text = ''

        with open(config_path, 'r') as config_file:
            config_text = config_file.read()

        if not config_text:
            logging.critical('given config path appears to be empty')
            sys.exit(42)

        try:
            yaml_config = yaml.load(config_text, yaml.FullLoader)
        except yaml.YAMLError as e:
            if hasattr(e, 'problem_mark'):
                mark = e.problem_mark
                logging.critical(f'got an error parsing YAML file at: ({mark.line+1}{mark.column+1})')
            else:
                logging.critical('some error was encountered during YAML parsing')

            sys.exit(42)

        try:
            self._auth_token = yaml_config['Auth_token']
        except KeyError as e:
            logging.critical('failed to fetch auth token from config file')

            sys.exit(42)

        logging.debug(f'got telegram auth token from config: `{self._auth_token}`')
    
    def start(self):
        if not self._auth_token:
            logging.critical('missing auth token. Make sure to read config before trying to start bot')

            sys.exit(42)

        logging.info('trying to start bot..')

        