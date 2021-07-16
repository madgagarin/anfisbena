import asyncio
from asyncio import new_event_loop
from threading import Thread

from aiogram.utils import executor
from flask_caching import Cache
from flask import Flask, render_template, send_from_directory, abort, send_file, url_for, render_template_string

# from images import gen_thumbnails
# from misc import cache, bot
from uwsgidecorators import thread

from misc import db, bot as bott, dp
from flask_bootstrap import Bootstrap

from tools import startup, shutdown

app = Flask(__name__)
bootstrap = Bootstrap(app)

# cache.init_app(app)  # инициализация кэша
# @app.before_first_request декоратор для функции запускаемой при старте

import handlers
import keyboards


@thread
def sa():
    loop = new_event_loop()
    asyncio.set_event_loop(loop)
    # loop.run_in_executor(executor.start_polling(dp, on_startup=startup, on_shutdown=shutdown, skip_updates=True))
    loop.run_until_complete(executor.start_polling(dp, on_startup=startup, on_shutdown=shutdown, skip_updates=True))


sa()


# хендлер корневой страницы
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
# @cache.cached(timeout=600)
def index():
    content_h1 = 'Привет!'
    content = 'На следующих вкладках ссылка на бота и сообщения от него'

    return render_template('index.html', title='Начало', content_h1=content_h1, content=content)


@app.route('/bot')
def bot():
    db_cursor = db.cursor()
    db_cursor.execute('SELECT * FROM info')
    data = db_cursor.fetchall()  # or use fetchone()
    db_cursor.execute('SELECT * FROM bot')
    bot_name = db_cursor.fetchall()  # or use fetchone()
    db_cursor.close()
    if not data:
        text = 'Боту пока не прислали ни одного сообщения'
    else:
        text = f'Бот получил сообщений: {len(data)}'
    return render_template('bot.html', title='Бот', bot_name=bot_name[0][0], text=text)


@app.route('/messages')
def messages():
    db_cursor = db.cursor()
    db_cursor.execute('SELECT * FROM info')
    data = db_cursor.fetchall()  # or use fetchone()
    print(data)
    db_cursor.close()
    return render_template('messages.html', title='Сообщения', messages=data)
