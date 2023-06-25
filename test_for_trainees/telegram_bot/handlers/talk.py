from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.states import Menu, Talk
from config import bot
from generating.talk.talk import generate_chat

router = Router()
prompt = {}


@router.message(Talk.wait_prompt)
async def prompt_given(message: Message, state: FSMContext):
    global prompt
    userid = message.from_user.id
    prompt[userid] = message.text
    text = await generate_chat(prompt=prompt[userid], userid=userid)
    await bot.send_message(chat_id=message.from_user.id, text=text)
    await state.set_state(Talk.wait_prompt)

@router.message(Talk.stop_talk)
async def stop_talk(message: Message, state: FSMContext):
    global prompt
    userid = message.from_user.id
    if userid in prompt:
        del prompt[userid]
    await state.finish()
    await bot.send_message(chat_id=message.from_user.id, text='Conversation ended.')


