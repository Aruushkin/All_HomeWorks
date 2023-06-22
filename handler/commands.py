from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import bot, dp


# @dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    await bot.send_message(message.chat.id, f'Добро пожаловать! {message.from_user.full_name}')


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message) -> None:
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton('NEXT', callback_data='next_button_1')
    markup.add(next_button)
    question = 'Столица Канады?'
    answers = [
        'Торонто',
        'Амстердам',
        'Вашингтон',
        'Оттава',
        'Ванкувер',
    ]

    # await bot.send_poll()
    await message.answer_poll(
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='Теперь будешь знать.',
        open_period=15,
        reply_markup=markup,
        )


# @dp.message_handler(commands=['cat'])
async def cat_handler(message: types.Message) -> None:
    await message.answer_photo(
        photo='https://i.cbc.ca/1.5359228.1577206958!/fileImage/httpImage/image.jpg_gen/derivatives/16x9_940/smudge-the-viral-cat.jpg'

        )


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(cat_handler, commands=['cat'])
