from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.replay import main_kb
from misc import dp


# Реакция на команду /start
@dp.message_handler(commands=['start'], state='*')
async def start_command(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Привет! Напиши что-нибудь')


# Реакция на команду /help
@dp.message_handler(commands=['help'], state='*')
async def help_command(message: types.Message):
    await message.reply('Не знаешь что написать - просто отправь котика', reply_markup=main_kb)
