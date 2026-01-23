from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio


bot = Bot(token="ff")
dp = Dispatcher()

# Клавиатура
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Салям"), KeyboardButton(text="Памаги")]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,  # Исчезает после нажатия
)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Выберите действие:", reply_markup=keyboard)

@dp.message(F.text == "Привет")
async def hello(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())