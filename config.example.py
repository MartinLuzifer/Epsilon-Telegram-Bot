from os import getenv

TELEGRAM_BOT_API_KEY = getenv('TELEGRAM_BOT_API_KEY')

MONGODB = { # do not change the sequence
    'MONGODB_USER': getenv('MONGODB_USER'),
    'MONGODB_PASS': getenv('MONGODB_PASS'),
    'MONGODB_ADDR': getenv('MONGODB_ADDR'),
    'MONGODB_PORT': getenv('MONGODB_PORT'),
}
MONGODB_URL = 'mongodb://{}:{}@{}:{}'.format(*MONGODB.values())

