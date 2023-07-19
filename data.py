from aiogram import Bot,Dispatcher,executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot=Bot("ТОКЕН")
dp=Dispatcher(bot, storage=MemoryStorage())