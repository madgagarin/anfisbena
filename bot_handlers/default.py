from aiogram import types
from flask import url_for

from misc import dp, db, bot, admin_id
from aiogram.types.message import ContentType
from tools import get_img_url


@dp.message_handler(text='Статистика')
async def echo(message: types.Message):
    db_cursor = db.cursor()
    db_cursor.execute('SELECT * FROM info')
    data = db_cursor.fetchall()  # or use fetchone()
    db_cursor.close()
    xm = 0
    for i in data:
        if i[1] == message.chat.id:
            xm += 1
    if len(data) == 0:
        await message.answer(f'Опубликованных сообщений нет')
    else:
        await message.answer(f'Всего сообщений опубликовано: {len(data)}\nИз них ваших: {xm}')
    await bot.send_message(admin_id, f'От {message.chat.username} запрошена статистика')


# Ответ на любой текст, кроме хендлеров выше
@dp.message_handler()
async def echo(message: types.Message):
    user_photos = await bot.get_user_profile_photos(message.chat.id, limit=1)
    if user_photos != 0:
        for f in user_photos['photos'][0]:
            if f['width'] < 200:
                user_photo_id = f['file_id']
                break
        await bot.download_file_by_id(user_photo_id, f'static/avatars/{message.chat.id}.jpg')
    else:
        await bot.download_file_by_id('AgACAgIAAxkBAANNYPSPOERDuuVtJwSahumenl9AZokAAqu0MRtNYqhLqmQPjVVNp6wBAAMCAANzAAMgBA', f'static/avatars/{message.chat.id}.jpg')
    db_cursor = db.cursor()
    db_cursor.execute(
        f'INSERT INTO info VALUES(\'{message.date}\', \'{message.chat.id}\', \'{message.chat.username}\', \'{message.text}\', NULL)')
    db.commit()
    db_cursor.close()
    await message.answer('Ok')
    await bot.send_message(admin_id, f'От {message.chat.username} отправлено сообщение:\n{message.text}')


# Ответ на любой контент, кроме того, что выше
@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(message: types.Message):
    print(message.chat.id)
    await message.reply('Я не знаю, что с этим делать. Если что-то непонятно, есть команда /help')
    await bot.send_message(admin_id, f'От {message.chat.username} отправлено что-то')
