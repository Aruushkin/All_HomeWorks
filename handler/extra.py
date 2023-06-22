from aiogram import types, Dispatcher
from config import dp, bot


@dp.message_handler()
async def process_empty_message(message: types.Message):
    try:
        number = float(message.text)
        squared = number ** 2
        await message.answer(f'{squared}')
    except ValueError:
        await message.answer("Пожалуйста введите корректное число.")


# @dp.message_handler(content_types=['text'])
async def echo_text(message: types.Message) -> None:
    await bot.send_message(message.chat.id, message.text)


# @dp.message_handler(content_types=['sticker'])
async def echo_sticker(message: types.Message) -> None:
    await bot.send_sticker(message.chat.id, message.sticker.file_id)


def register_handlers_extra(dp: Dispatcher):
    # dp.register_message_handler(echo_text)
    dp.register_message_handler(echo_text, content_types=['text'])
    dp.register_message_handler(echo_sticker, content_types=['sticker'])
    dp.register_message_handler(process_empty_message, )

