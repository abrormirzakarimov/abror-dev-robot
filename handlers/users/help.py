from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from data.config import MEMBER_ID
from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "/set_photo - Guruhni rasmini o'zgartirish",
            "/set_title - Guruhni nomini o'zgartirish",
            "/set_description - Guruhni haqidagi ma'lumotni o'zgartirish"
            )
    
    await message.answer("\n".join(text))
    await message.answer(MEMBER_ID)