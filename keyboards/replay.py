from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# Стартовые кнопки
button_main_menu = KeyboardButton('Статистика')
main_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_main_menu)

# Клавиатурная кнопка назад
button_back = KeyboardButton('⬅ Назад')
back_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_back)
