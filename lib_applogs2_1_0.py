import logging
from logging.handlers import TimedRotatingFileHandler
import os
import json


with open('settings.json', 'r') as file:
    settings = json.load(file)

logs_path = ""
log_name = ""
for item in settings:
    if 'logs_path' in item:
        logs_path = item['logs_path']
        print(logs_path)
    if 'log_name' in item:
        log_name = item['log_name']

if logs_path and log_name:
    full_log_path = os.path.join(logs_path, log_name)
    print(f"Full log path: {full_log_path}")
else:
    print("logs_path or log_name is missing in the settings.json")


LogFolder = './logs'

print("-- Checking log directory...")

if os.path.exists(LogFolder):
    print(f"-- The directory {logs_path} exists.")
else:
    print(f"-- The directory {logs_path} does not exist.")
    print(f"-- Directory created.")
    os.mkdir(f'./{logs_path}')

full_log_path = f'{logs_path}/{log_name}'
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
handler = TimedRotatingFileHandler(full_log_path, when="d", interval=1, backupCount=7, encoding='utf-8')
formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s: %(message)s', datefmt='%d/%m/%Y %H:%M:%S -')
handler.setFormatter(formatter)
logger.addHandler(handler)

def log_print(level, message):
    print(message)
    if level == 'info':
        logger.info(message)
    elif level == 'warning':
        logger.warning(message)
    elif level == 'debug':
        logger.debug(message)
    elif level == 'error':
        logger.error(message)
    elif level == 'critical':
        logger.critical(message)
    else:
        logger.log(logging.NOTSET, message)