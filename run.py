import asyncio
from asyncio import new_event_loop
from threading import Thread

from aiogram import executor

from index import app
from misc import dp
from tools import shutdown, startup
from uwsgidecorators import thread


@thread
def sa():
    loop = new_event_loop()
    asyncio.set_event_loop(loop)
    # loop.run_in_executor(executor.start_polling(dp, on_startup=startup, on_shutdown=shutdown, skip_updates=True))
    loop.run_until_complete(executor.start_polling(dp, on_startup=startup, on_shutdown=shutdown, skip_updates=True))


if __name__ == "__main__":
    # Thread(target=new_event_loop().run_until_complete, args=(abot.run(),),
    #    daemon=True).start()  # Запуск дополнительного потока с новой асинхронной петлей внутри
    #Thread(target=sa, args=(), daemon=True).start()  # Запуск дополнительного потока
    app.run()
