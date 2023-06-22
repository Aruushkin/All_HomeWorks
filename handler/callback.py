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


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text='next_button_1')
    dp.register_callback_query_handler(quiz_3, text='next_button_2')
    dp.register_callback_query_handler(quiz_4, text='next_button_3')
    dp.register_callback_query_handler(finish, text='next_button_4')

