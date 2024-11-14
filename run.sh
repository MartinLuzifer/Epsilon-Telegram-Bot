docker compose up -d mongo && \
docker compose up -d mongo-express && \
docker build --tag epsilon-telegram-bot . && \
docker compose up -d epsilon-telegram-bot && \
docker compose logs epsilon-telegram-bot --follow --tail 50
