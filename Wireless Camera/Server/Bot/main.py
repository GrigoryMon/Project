from aiogram import Bot, executor
from create import dp,bot
from handlers import client
import cv2,base64
import numpy as np
import asyncio,aiohttp
import datetime


delay = 20

async def on_startup(_):
    print('Bot online')
    

async def requestdata():
    while True:

        url = 'http://127.0.0.1:8000/'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:

                d = await response.json()
                data =d['content']
                if data:
                    
                    await client.send_notice(data)
                    
                
        await asyncio.sleep(60)

client.register_handlers_client(dp)
#admin.register_handlers_admin(dp)

if __name__=='__main__':
    
    loop = asyncio.get_event_loop()
    loop.create_task(requestdata())
    executor.start_polling( dp, skip_updates=True, on_startup=on_startup, loop=loop )
    