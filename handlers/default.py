from aiogram import types
from misc import dp, db, bot
from aiogram.types.message import ContentType
from tools import get_img_url


@dp.message_handler(text='Отправить случайное фото котика')
async def echo(message: types.Message):
    db_cursor = db.cursor()
    cat_url = get_img_url('cat')
    db_cursor.execute(
        f'INSERT INTO info VALUES(\'{message.date}\', \'{message.chat.id}\', \'{message.chat.username}\', NULL, \'{cat_url}\')')
    db.commit()
    db_cursor.close()
    await message.answer('Случайный котик есть')


# Ответ на любой текст, кроме хендлеров выше
@dp.message_handler()
async def echo(message: types.Message):
    db_cursor = db.cursor()
    db_cursor.execute(
        f'INSERT INTO info VALUES(\'{message.date}\', \'{message.chat.id}\', \'{message.chat.username}\', \'{message.text}\', NULL)')
    db.commit()
    db_cursor.close()
    await message.answer('Опубликовал')


# Ответ на любой контент, кроме того, что выше
@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(message: types.Message):
    await message.reply('Я не знаю, что с этим делать. Если что-то непонятно, есть команда /help')
