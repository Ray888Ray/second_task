from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup
from aiogram.fsm.context import FSMContext
from states.states import Menu, Text, Image
from config import bot
from generating.image.images import generate_img
router = Router()
global prompt
global num


def is_int(str):
    if str is None:
        return False
    try:
        int(str)
        return True
    except ValueError:
        return False


@router.message(Image.wait_prompt)
async def prompt_given(message: Message, state: FSMContext):
    global prompt
    prompt = message.text
    await state.set_state(Image.wait_num)
    await message.answer(text = 'Write number of images: ')


@router.message(Image.wait_num)
async def nums_given(message: Message, state: FSMContext):
    if is_int(message.text):
        await bot.send_message(chat_id=message.from_user.id, text='Your images:')
        for i in range(int(message.text)):
            photo_url = await generate_img(prompt=prompt)
            if photo_url:
                await bot.send_photo(chat_id=message.from_user.id, photo=photo_url)
            else:
                await bot.send_message(chat_id=message.from_user.id, text='Error')
        await state.set_state(Menu.menu)
        await bot.send_message(chat_id=message.from_user.id, text='Generation ended. Use /image, /text, or /talk')
    else:
        await message.answer('Write a correct number')
