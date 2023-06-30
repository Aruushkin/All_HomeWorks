from aiogram import types, Dispatcher
from config import dp, bot


# @dp.message_handler(content_types=['text'])
# async def echo_text(message: types.Message) -> None:
#     await bot.send_message(message.chat.id, message.text)


# @dp.message_handler(content_types=['sticker'])
async def echo_sticker(message: types.Message) -> None:
    await bot.send_sticker(message.chat.id, message.sticker.file_id)


def register_handlers_extra(dp: Dispatcher):
    # dp.register_message_handler(echo_text)
    # dp.register_message_handler(echo_text, content_types=['text'])
    dp.register_message_handler(echo_sticker, content_types=['sticker'])

