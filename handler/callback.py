from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# @dp.callback_query_handler(text='next_button')
async def quiz_2(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton('NEXT', callback_data='next_button_2')
    markup.add(next_button)
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
        reply_markup=markup,

    )


async def quiz_3(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton('NEXT', callback_data='next_button_3')
    markup.add(next_button)
    question = 'Какой язык программирования самый популярный?'
    answers = [
        'Python',
        'JavaScript',
        'Java',
        'C++',
        'TypeScript',
    ]

    await callback.message.answer_poll(
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='Теперь будешь знать.',
        open_period=15,
        reply_markup=markup,

    )


async def quiz_4(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton('NEXT', callback_data='next_button_4')
    markup.add(next_button)
    question = 'Кто открыл америку?'
    answers = [
        'Ньютон',
        'Колумб',
        'тесла',
        'илон маск',
        'путин',
    ]

    await callback.message.answer_poll(
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='Теперь будешь знать.',
        open_period=15,
        reply_markup=markup,

    )


async def finish(callback: types.CallbackQuery):
    await callback.message.answer('Это все!')

# -------------------------

async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('Нажми меня!', callback_data='button_pressed'))

    await message.answer('Привет! Нажми кнопку, чтобы продолжить.', reply_markup=keyboard)


async def handle_button_pressed(callback_query: types.CallbackQuery):
    await callback_query.answer('Кнопка была нажата!')
    await callback_query.message.answer('Ты нажал кнопку!')


async def help(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('ПОМОГИ!', callback_data='button_pressed'))

    await message.answer('Это помощь. Чем я могу тебе помочь?', reply_markup=keyboard)


async def handle_help_button(callback_query: types.CallbackQuery):
    await callback_query.answer('Кнопка "ПОМОГИ!" была нажата!')
    await callback_query.message.answer('Ты нажал кнопку "Помощь"!')


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text='next_button_1')
    dp.register_callback_query_handler(quiz_3, text='next_button_2')
    dp.register_callback_query_handler(quiz_4, text='next_button_3')
    dp.register_callback_query_handler(finish, text='next_button_4')
    dp.register_message_handler(start, commands=['starttt'])
    dp.register_callback_query_handler(handle_button_pressed, text='button_pressed')
    dp.register_message_handler(help, commands=['help'])
    dp.register_callback_query_handler(handle_help_button, text='help_button')

