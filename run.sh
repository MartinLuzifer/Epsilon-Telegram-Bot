docker compose up -d mongo
docker compose up -d mongo-express
docker compose up -d epsilon-telegram-bot

docker compose logs epsilon-telegram-bot --follow --tail 50
