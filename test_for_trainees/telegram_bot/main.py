from generating.image import images
from aiogram import Bot, types, Dispatcher
import asyncio
import logging
import config
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import start, image, text, talk


logging.basicConfig(level=logging.INFO)


async def on_startup(_):
    print('Online')


# Запуск бота
storage = MemoryStorage()
global dp
async def main():
    global dp
    
    bot = config.bot
    dp = Dispatcher(bot = bot, storage = storage)
    dp.include_router(start.router)
    dp.include_router(image.router)
    dp.include_router(text.router)
    dp.include_router(talk.router)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await(dp.start_polling(bot))
    except:
        pass
    

if __name__ == "__main__":
    asyncio.run(main())
    
    










print('Would yout like to generate image(1), text(2) or chat(3)? Print 1, 2 or 3 ')
ans = int(input())
if(ans == 1):
    images.generate_img()
elif(ans == 2):
    text.generate_text()
elif (ans == 3):
    talk.generate_chat()
else:
    print('Write the correct answer')