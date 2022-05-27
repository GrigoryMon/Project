from typing import Text
from aiogram import Dispatcher, types
from numpy import equal
from create import dp, bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import requests, aiohttp, base64,cv2,os
from aiogram.dispatcher.filters import Text
from keyboards.client import kb
import numpy as np

class Reg(StatesGroup):
    Camera = State()
    Camera2 = State()

async def send_notice(data):
    for elem in data:
        string = elem['image']
        jpg_original = base64.b64decode(string)
        jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
        img = cv2.imdecode(jpg_as_np, flags=1)
        cv2.imwrite('./0.jpg', img)
        photo = open('./0.jpg', 'rb')
        await bot.send_photo(elem['user'],photo)
        os.remove('./0.jpg')
        
    
async def reg_camera1(message: types.Message, state: FSMContext):
    await Reg.Camera.set()
    await message.answer('Enter Camera ID')

async def reg_user(message: types.Message):
    url = 'http://127.0.0.1:8000/Register/'
    async with aiohttp.ClientSession() as session:
        data = {'user':{'telegram_id': message.from_user.id}}
        await session.post(url, json = data) 
    await message.reply('Thanks!', reply_markup=kb.kb)

async def reg_camera(message:types.Message, state: FSMContext):
    url = 'http://127.0.0.1:8000/Register/'
    async with aiohttp.ClientSession() as session:
        data = {'camera':{'camera_id': int(message.text)}}
        await session.post(url, json = data)
    await state.finish() 
    await message.reply('Thanks!')

async def start(message: types.Message):
    await message.answer('/register')

async def add_camera(message:types.Message, state: FSMContext):
    await Reg.Camera2.set()
    await message.answer('Enter Camera ID')

async def enter_camera(message:types.Message, state: FSMContext):
    url = 'http://127.0.0.1:8000/AddCamera/'
    async with aiohttp.ClientSession() as session:
        data = {'data':{'camera': int(message.text), 'user': message.from_user.id}}
        await session.post(url, json = data)
    await state.finish() 
    await message.reply('Thanks!')

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(reg_user, commands=['register'])
    dp.register_message_handler(reg_camera1, commands=['registerCamera'], state=None)
    dp.register_message_handler(reg_camera, state=Reg.Camera)
    dp.register_message_handler(add_camera, commands=['AddCamera'], state=None)
    dp.register_message_handler(enter_camera, state=Reg.Camera2)