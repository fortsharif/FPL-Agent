FROM cimg/python:3.9.6

WORKDIR /app

RUN mkdir db && touch db/fpl-bot.db

COPY . /app

RUN python3.9 -m pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt