#!/bin/bash

# Запуск нескольких экземпляров Streamlit на разных портах
# Использование: ./run_multi.sh [кол-во экземпляров] [начальный_порт]

COUNT=${1:-1}
START_PORT=${2:-8501}

for ((i=0; i<$COUNT; i++)); do
  PORT=$((START_PORT + i))
  # Проверяем, свободен ли порт
  if lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null ; then
    echo "Порт $PORT занят, ищу следующий..."
    # Ищем следующий свободный порт
    while lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null ; do
      PORT=$((PORT + 1))
    done
  fi
  echo "Запускаю экземпляр на порту $PORT..."
  nohup streamlit run admin_panel.py --server.port $PORT > streamlit_$PORT.log 2>&1 &
done

echo "Все экземпляры запущены. Логи: streamlit_<порт>.log" 