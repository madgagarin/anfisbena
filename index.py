import asyncio
from asyncio import new_event_loop
from threading import Thread

from aiogram.utils import executor
from flask_caching import Cache
from flask import Flask, render_template, send_from_directory, abort, send_file, url_for, render_template_string

# from images import gen_thumbnails
# from misc import cache, bot

from misc import db, bot as bott, dp
from flask_bootstrap import Bootstrap

from tasks import sa
from tools import startup, shutdown

app = Flask(__name__)
bootstrap = Bootstrap(app)

# cache.init_app(app)  # инициализация кэша
# @app.before_first_request декоратор для функции запускаемой при старте

import bot_handlers
import keyboards


@app.before_first_request
def bfr():
    sa()


# хендлер корневой страницы
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
# @cache.cached(timeout=600)
def index():
    content_h1 = 'Приветствую!'
    content = 'Отправь сообщение боту и посмотри его на вкладке поток'
    return render_template('index.html', title='Anfisbena', content_h1=content_h1, content=content)


@app.route('/bot')
def bot():
    db_cursor = db.cursor()
    db_cursor.execute('SELECT * FROM info')
    data = db_cursor.fetchall()  # or use fetchone()
    db_cursor.execute('SELECT * FROM bot')
    bot_name = db_cursor.fetchall()  # or use fetchone()
    db_cursor.close()
    if data is None:
        text = 'Боту пока не прислали ни одного сообщения'
        ids = None
    else:
        text = f'Всего сообщений: {len(data)}'
        ids = {}
        for ms in data:
            if ms[2] in ids:
                ids[ms[2]] += 1
            else:
                ids[ms[2]] = 1
    return render_template('statistics.html', title='Статистика', bot_name=bot_name[0][0], text=text, ids=ids)


@app.route('/messages')
def messages():
    db_cursor = db.cursor()
    db_cursor.execute('SELECT * FROM info')
    data = db_cursor.fetchall()  # or use fetchone()
    db_cursor.close()
    return render_template('messages.html', title='Поток', messages=data)
