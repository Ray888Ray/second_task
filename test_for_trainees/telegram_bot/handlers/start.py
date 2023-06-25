from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup
from aiogram.fsm.context import FSMContext
from states.states import Menu, Text, Image, Talk
from config import bot

router = Router()



@router.message(Command(commands=["start"]))
async def cmd_start(message: Message, state: FSMContext):
    global id
    id = str(message.from_user.id)
    await message.answer(text='Use /image /text or /talk')
    await state.set_state(Menu.menu)    


@router.message(Command(commands=["help"]))
async def help(message: Message):
    await message.answer(text = 'Hello! Use /image /text or /talk')

@router.message(Command(commands=['image']))
async def date_info(message: Message, state: FSMContext):
    id = str(message.from_user.id)
    await state.set_state(Image.wait_prompt)
    await message.answer(text='Write your prompt')

@router.message(Command(commands=['text']))
async def ask_cancel_reminder(message: Message, state: FSMContext):
    await state.set_state(Text.wait_prompt)
    await message.answer(text='Write your prompt')

@router.message(Command(commands=['talk']))
async def start_conversation(message: Message, state: FSMContext):
    await state.set_state(Talk.wait_prompt)
    await message.answer(text='You can now start conversation: ')

@router.message(Command(commands=['stop_talk']))
async def stop_conversation(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.set_state(Menu.menu)
    await message.reply('Conversation stopped.')
    await bot.send_message(chat_id=message.from_user.id, text='Generation ended. Use /image, /text, or /talk')


@router.message(Command(commands=['refresh']))
async def refresh(message: Message, state: FSMContext):
    await state.set_state(Menu.menu)
    await message.answer('Refreshed. Use /help to see commands')