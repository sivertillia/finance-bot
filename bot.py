from aiogram import Bot, Dispatcher, executor, types
import random

import config

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Рандом бот")

@dp.message_handler()
async def random_bot(message: types.Message):
    random_password = "random"
    await message.answer(random_password)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)