import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot

async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.chat.id
    await bot.send_message(chat_id=chat_id, text="Получил твою Айди))")

async def birthday():
    await bot.send_message(chat_id=chat_id, text="Сегодня Днюха!")

async def shceduler():
    aioschedule.every().saturday.do(birthday)

def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'Birthday' in word.text)