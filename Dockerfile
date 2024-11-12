FROM python:3.10.12

RUN mkdir -p /python/telegramBot
WORKDIR /python/telegramBot

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .
COPY config.py .
COPY router.py .
COPY .env .

ENTRYPOINT ["python", "main.py"]