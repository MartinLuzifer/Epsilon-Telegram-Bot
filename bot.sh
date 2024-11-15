#!/usr/bin/bash
# shellcheck disable=SC1009
# shellcheck disable=SC2194

operation=$1

startBot () {
  docker compose up -d mongo mongo-express && \
  sleep 2

  docker build --tag epsilon-telegram-bot . && \
  docker compose up -d epsilon-telegram-bot && \
  docker compose logs epsilon-telegram-bot --follow --tail 50
}

stopBot () {
  docker compose down --volumes --remove-orphans
  docker image rm epsilon-telegram-bot

  echo "Containers list" && docker ps -a
  echo "Images list" && docker images -a
}

case "$operation" in
  ( "run" | "start" ) echo "Try run Bot" && startBot ;;
  ( "down" | "stop" ) echo "Try down Bot" && stopBot ;;
  ( * ) echo "command $operation  not support" ;;
esac

