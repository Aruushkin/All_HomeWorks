from aiogram import executor
import logging
from config import dp
from handler import commands, callback, extra, admin


commands.register_handlers_commands(dp)
callback.register_handlers_callback(dp)
extra.register_handlers_extra(dp)
admin.game_message_handler(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
