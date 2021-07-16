from index import app
from aiogram import executor
from misc import dp
from tools import shutdown, startup
from threading import Thread

# Импорт пакетов с хэндлерами и клавиатурами
import handlers
import keyboards

# Запуск бота
if __name__ == "__main__":
    Thread(target=app.run, args=(), daemon=True).start()  # Запуск дополнительного потока
    executor.start_polling(dp, on_startup=startup, on_shutdown=shutdown, skip_updates=True)  # Запуск основного потока с ботом