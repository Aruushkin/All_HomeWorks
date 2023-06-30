from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import bot, dp

from handler.parser import serials, mult, anime


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    await bot.send_message(message.chat.id, f'Добро пожаловать! {message.from_user.full_name}')


@dp.message_handler(commands=['quiz'])
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


@dp.message_handler(commands=['cat'])
async def cat_handler(message: types.Message) -> None:
    await message.answer_photo(
        photo='https://i.cbc.ca/1.5359228.1577206958!/fileImage/httpImage/image.jpg_gen/derivatives/16x9_940/smudge-the-viral-cat.jpg'

        )

@dp.message_handler(commands=['number'])
async def process_number_command(message: types.Message):
    try:
        # Получаем аргументы команды
        command_args = message.get_args()

        # Проверяем, что введены аргументы команды
        if not command_args:
            await message.answer("Пожалуйста, укажите число и степень после команды.")
            return

        # Разделяем аргументы на число и степень
        args = command_args.split()

        if len(args) != 2:
            await message.answer("Пожалуйста, укажите число и степень после команды.")
            return

        number = float(args[0])
        power = float(args[1])

        result = number ** power
        await message.answer(f"Результат: {result}")

    except ValueError:
        await message.answer("Пожалуйста, введите корректное число и степень.")


async def parser_serials(message: types.Message):
    data = serials.parser()
    for i in data:
        await bot.send_message(message.from_user.id,
                               f"{i['title']}\n\n{i['link']}")

async def parser_multiki(message: types.Message):
    data = mult.parser()
    for i in data:
        await bot.send_message(message.from_user.id,
                               f"{i['title']}\n\n{i['link']}")

async def parser_anime(message: types.Message):
    data = anime.parser()
    for i in data:
        await bot.send_message(message.from_user.id,
                               f"{i['title']}\n\n{i['link']}")

def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(cat_handler, commands=['cat'])
    dp.register_message_handler(process_number_command, commands=['number'])
    dp.register_message_handler(parser_serials, commands=['serials'])
    dp.register_message_handler(parser_multiki, commands=['multiki'])
    dp.register_message_handler(parser_anime, commands=['anime'])
