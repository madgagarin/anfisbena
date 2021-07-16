from sqlite3 import connect
from flask_caching import Cache
import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # Тип хранилища состояний
from aiogram.contrib.middlewares.logging import LoggingMiddleware  # Встроенное в библиотеку aiogram логирование


# Настройка кэша
cache = Cache(config={'CACHE_TYPE': 'UWSGICache', 'CACHE_UWSGI_NAME':'mycache', "CACHE_DEFAULT_TIMEOUT": 600})  # настройка кэширования

# Инициализация бота и диспетчера
bot = Bot(token='1355733455:AAFgBVofZciOK6BYwUtE65IOV-gLJFCC2gw')
dp = Dispatcher(bot, storage=MemoryStorage())  # Указание типа хранилища состояний в оперативную память

# Подключение базы данных
db = connect(':memory:', check_same_thread=False)  # :memory: - в оперативную память

# Логирование
logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())

