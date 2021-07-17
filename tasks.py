import asyncio
from asyncio import new_event_loop

from aiogram.utils import executor
from uwsgidecorators import spool, spoolforever

from misc import dp
from tools import startup, shutdown


@spoolforever
def sa():
    loop = new_event_loop()
    asyncio.set_event_loop(loop)
    # loop.run_in_executor(executor.start_polling(dp, on_startup=startup, on_shutdown=shutdown, skip_updates=True))
    loop.run_until_complete(executor.start_polling(dp, on_startup=startup, on_shutdown=shutdown, skip_updates=True))
