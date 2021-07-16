from asyncio import sleep, run_coroutine_threadsafe, get_event_loop
from json import loads

import requests as requests
from aiogram.utils.exceptions import MessageToForwardNotFound
from requests import get

from misc import db, bot, Dispatcher
from logging import info, error


# Функция срабатывающая при запуске бота. Создает базу данных в памяти, получая данные из db_backup_message
async def startup(dispatcher: Dispatcher):
    from sys import version_info
    info(' Запуск!')
    bot_name = (await bot.get_me())['username']
    db_cursor = db.cursor()
    # Создание базы данных
    db_cursor.execute('CREATE TABLE info(data_time text NOT NULL, user_id integer NOT NULL, user_name text, '
                      'answer text, img text)')
    db_cursor.execute('CREATE TABLE bot(bot_name text NOT NULL)')
    db_cursor.execute(f"INSERT INTO bot VALUES(\'{bot_name}\')")
    db.commit()
    # Вывод версии Python
    r = version_info.releaselevel
    f = '' if r == 'final' else r
    info(f' Python {version_info.major}.{version_info.minor}.{version_info.micro} {f}')
    # Вывод версии SQLite
    db_cursor.execute("select sqlite_version();")  # Вывод информации о версии SQLite
    info(f' SQLite {db_cursor.fetchall()[0][0]}')
    db_cursor.close()


# Функция срабатывающая при отключении бота.
async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()  # Закрытие соединений с хранилищем состояний бота
    await dispatcher.storage.wait_closed()
    db.close()
    info(' Пока!')


def get_img_url(text):
    response = get(f'https://some-random-api.ml/img/{text}')  # Запрос картинки
    json_data = loads(response.text)  # Извлекаем JSON
    return json_data['link']
