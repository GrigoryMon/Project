from typing import Text
from aiogram import Dispatcher, types
from numpy import equal
from create import dp, bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import requests, aiohttp, base64
from aiogram.dispatcher.filters import Text

async def send_notice(data):
    url = 'http://127.0.0.1:8000'
    async with aiohttp.ClientSession() as session:
            async with session.get('url') as response:

                data = await response.json()['content']
    for elem in data:
        img = 
        await bot.send_message(elem['user'], e)

async def reg(message: types.Message):
    print(message.from_user.id)
    await message.reply('Thanks!')

async def start(message: types.Message):
    await message.answer('/register')

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(reg, commands=['register'])