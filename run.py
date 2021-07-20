import asyncio
from asyncio import new_event_loop
from threading import Thread

from aiogram import executor

from index import app
from misc import dp
from tasks import bot_start
from tools import shutdown, startup
from uwsgidecorators import thread



if __name__ == "__main__":
    # Thread(target=new_event_loop().run_until_complete, args=(abot.run(),),
    #    daemon=True).start()  # Запуск дополнительного потока с новой асинхронной петлей внутри
    #Thread(target=sa, args=(), daemon=True).start()  # Запуск дополнительного потока
    app.run()
