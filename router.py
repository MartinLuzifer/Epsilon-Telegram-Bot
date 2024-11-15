from aiogram import Router, html
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from keyboard import mainKeyboard

mainRouter = Router(name='main_Router')
baseRouter = Router(name='base_Router')

class FSM1(StatesGroup):
    name = State()
    mail = State()
    number = State()


# ===>>> BASE ROUTES
@baseRouter.message(CommandStart())
async def start(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(f'Hello, {html.bold(message.from_user.full_name)}!')
    await message.answer(f'If you want send tickets enter /ticket:', reply_markup=mainKeyboard)

@baseRouter.message(Command('help'))
async def get_help(message: Message) -> None:
    answer = '''Как пользоваться ботом:
    /start - Запустить бота
    /help  - Вывести справку
    '''
    await message.answer(answer)
# ===>>>


# ===>>> MAIN ROUTES
@mainRouter.message(Command('ticket'))
async def registration_step_one(message: Message, state: FSMContext) -> None:
    await state.set_state(FSM1.mail)
    await message.reply(text='please, send your email address: ')

@mainRouter.message(FSM1.mail)
async def registration_step_two(message: Message, state: FSMContext) -> None:
    await state.update_data({'mail': message.text})
    await state.set_state(FSM1.name)
    await message.reply(text='please, send your name')

@mainRouter.message(FSM1.name)
async def registration_step_three(message: Message, state: FSMContext) -> None:
    await state.update_data({'name': message.text})
    data = await state.get_data()
    await message.answer(text=f'{data}')


# ===>>> *
@mainRouter.message()
async def echo_handler(message: Message) -> None:
    await message.answer('Enter "/help" if you need help')

