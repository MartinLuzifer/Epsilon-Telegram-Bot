# Epsilon-Telegram-Bot

* Create config

```bash
cp config.example.py config.py
```

* Add Telegram Bot API token in .env
```bash
nano .env
```
change `TELEGRAM_BOT_API_KEY=` 

to `TELEGRAM_BOT_API_KEY=abcdefg1234...`

OR

```bash
nano config.py
```

change `TELEGRAM_BOT_API_KEY = values.get('TELEGRAM_BOT_API_KEY')` 

to `TELEGRAM_BOT_API_KEY=abcdefg1234...`
