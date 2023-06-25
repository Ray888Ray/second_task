from aiogram.fsm.state import StatesGroup, State


class Menu(StatesGroup):
    menu = State()


class Text(StatesGroup):
    wait_prompt = State()
    wait_creat = State()
    wait_num = State()
    wait_tok = State()


class Image(StatesGroup):
    wait_prompt = State()
    wait_num = State()


class Talk(StatesGroup):
    wait_prompt = State()
    stop_talk = State()
