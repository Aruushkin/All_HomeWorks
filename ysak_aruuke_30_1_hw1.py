from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from decouple import config
import logging

TOKEN = config('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


# @dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    await bot.send_message(message.chat.id, f'Добро пожаловать! {message.from_user.full_name}')
    # await message.answer('metod otveta')
    # await message.reply('otvet na konkretnoe sms')


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message) -> None:
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton('NEXT', callback_data='next_button')
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


# @dp.callback_query_handler(text='next_button')
async def quiz_2(callback: types.CallbackQuery):
    question = 'Какой по счету планета от Солнца является Земля?'
    answers = [
        'Первый',
        'Второй',
        'Третий',
        'Четвертый',
        'Пятый',
    ]

    await callback.message.answer_poll(
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Теперь будешь знать.',
        open_period=15,

    )


# @dp.message_handler(commands=['cat'])
async def cat_handler(message: types.Message) -> None:
    await message.answer_photo(
        photo='https://i.cbc.ca/1.5359228.1577206958!/fileImage/httpImage/image.jpg_gen/derivatives/16x9_940/smudge-the-viral-cat.jpg'

        )


# @dp.message_handler()
async def process_empty_message(message: types.Message):
    try:
        number = int(message.text)
        squared = number ** 2
        await message.answer(f'{squared}')
    except ValueError:
        await message.answer("Пожалуйста введите корректное число.")


# @dp.message_handler(content_types=['text'])
async def echo(message: types.Message) -> None:
    await bot.send_message(message.chat.id, message.text)


# @dp.message_handler(content_types=['sticker'])
async def echo(message: types.Message) -> None:
    await bot.send_sticker(message.chat.id, message.sticker.file_id)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
