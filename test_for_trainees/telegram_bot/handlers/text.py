from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup
from aiogram.fsm.context import FSMContext
from states.states import Menu, Text, Image
from config import bot
from generating.text.texts import generate_text
router = Router()
global prompt
global num
global temp
global tokens

def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def is_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

@router.message(Text.wait_prompt)
async def prompt_given(message: Message, state: FSMContext):
    global prompt
    prompt = message.text
    await state.set_state(Text.wait_num)
    await message.answer(text = 'Write number of requests: ')

@router.message(Text.wait_prompt)
async def prompt_given(message: Message, state: FSMContext):
    global prompt
    prompt = message.text
    await state.set_state(Text.wait_num)
    await message.answer(text='Write number of requests: ')


@router.message(Text.wait_num)
async def nums_given(message:Message, state:FSMContext):
    if(is_int(message.text)):
        global num
        num = int(message.text)
        await bot.send_message(chat_id = message.from_user.id, text = 'Write a lenght of text in tokens (max: 3500)')
        await state.set_state(Text.wait_tok)
    else: 
        message.answer('Write a correct number')

@router.message(Text.wait_tok)
async def nums_given(message:Message, state:FSMContext):
    if(is_int(message.text)):
        global tokens
        tokens = int(message.text)
        await bot.send_message(chat_id = message.from_user.id, text = 'Set a creativity (ex: 0.5). Best: 0.5')
        await state.set_state(Text.wait_creat)
    else: 
        message.answer('Write a correct number')

@router.message(Text.wait_creat)
async def nums_given(message:Message, state:FSMContext):
    global prompt
    if(is_float(message.text)):
        temp = float(message.text)
        await bot.send_message(chat_id = message.from_user.id, text = 'Your texts: ')
        for i in range(int(num)):
            text = await generate_text(promt=prompt, temperature=temp, max_tokens=tokens)
            await bot.send_message(chat_id = message.from_user.id, text = text)
        await state.set_state(Menu.menu)
        await bot.send_message(chat_id = message.from_user.id, text = 'Generation ended. Use /image or /text')
    else: 
        message.answer('Write a correct number')