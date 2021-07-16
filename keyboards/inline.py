from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Инлайновая кнопка назад
inline_button_back = InlineKeyboardButton('⬅ Назад', callback_data='back')
inline_back_kb = InlineKeyboardMarkup().add(inline_button_back)

