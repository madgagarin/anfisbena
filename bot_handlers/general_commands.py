from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.replay import main_kb
from misc import dp, bot, admin_id


# Реакция на команду /start
@dp.message_handler(commands=['start'], state='*')
async def start_command(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Привет! Напиши что-нибудь', reply_markup=main_kb)
    await bot.send_message(admin_id, f'От {message.chat.username} отправлена команда /start')


# Реакция на команду /help
@dp.message_handler(commands=['help'], state='*')
async def help_command(message: types.Message):
    await message.reply('Сообщение отправленное боту будет опубликовано https://anfisbena.herokuapp.com/', reply_markup=main_kb)
    await bot.send_message(admin_id, f'От {message.chat.username} отправлена команда /help')
