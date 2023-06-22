from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import Bot, types
from aiogram.dispatcher.filters.state import State, StatesGroup


class MentorForm(StatesGroup):
    Name = State()
    Direction = State()
    Age = State()
    Group = State()


async def start_mentor_creation(message: types.Message):
    await MentorForm.Name.set()
    await message.reply("Введите имя ментора:")


async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await MentorForm.Direction.set()
    await message.reply("Введите направление ментора:")


async def process_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await MentorForm.Age.set()
    await message.reply("Введите возраст ментора:")


async def process_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    await MentorForm.Group.set()
    await message.reply("Введите группу ментора:")


async def process_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
    await state.finish()
    await state.update_data(**data)
    await message.reply("Ментор успешно создан.")


def register_mentor_creation(dp: Dispatcher):
    dp.register_message_handler(start_mentor_creation, Command('create_mentor'))
    dp.register_message_handler(process_name, state=MentorForm.Name)
    dp.register_message_handler(process_direction, state=MentorForm.Direction)
    dp.register_message_handler(process_age, state=MentorForm.Age)
    dp.register_message_handler(process_group, state=MentorForm.Group)
