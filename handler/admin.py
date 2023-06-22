import random

from aiogram import types, Dispatcher
from config import dp, bot


@dp.message_handler(lambda message: message.text.startswith("game"))
async def game_message_handler(message: types.Message):
    emojis = ["⚽", "🏀", "🎯", "🎲", "🎰", "🎳"]
    random_emoji = random.choice(emojis)
    await message.answer(random_emoji, parse_mode='Markdown')


async def pin_message(message: types.Message):
    if message.reply_to_message:
        await message.reply_to_message.pin(disable_notification=True)
        await message.answer("Сообщение закреплено.")
    else:
        await message.answer("Эту команду можно использовать только в ответ на сообщение.")


def register_handlers_admin(dp: Dispatcher):
    dp.message_handler(game_message_handler)
    # dp.register_message_handler(pin, commands=['pin'])
    dp.register_message_handler(pin_message, commands=['pin'])
