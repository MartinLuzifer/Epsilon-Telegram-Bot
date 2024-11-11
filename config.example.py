from dotenv import dotenv_values

values = dotenv_values('.env')


TELEGRAM_BOT_API_KEY = values.get('TELEGRAM_BOT_API_KEY')

MONGODB = { # do not change the sequence
    'MONGODB_USER': values.get('MONGODB_USER'),
    'MONGODB_PASS': values.get('MONGODB_PASS'),
    'MONGODB_ADDR': values.get('MONGODB_ADDR'),
    'MONGODB_PORT': values.get('MONGODB_PORT'),
}
MONGODB_URL = 'mongodb://{}:{}@{}:{}'.format(*MONGODB.values())

print(TELEGRAM_BOT_API_KEY)