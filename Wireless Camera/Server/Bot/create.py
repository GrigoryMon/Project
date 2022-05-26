import logging
from aiogram import Bot,Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import socket


TOKEN = '5399617231:AAEmyK6sUp2ybuMcST0matbfRBmVVMnYYVo'

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
