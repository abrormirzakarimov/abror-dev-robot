from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from filters import isGroup
from data.config import MEMBER_ID,ADD_MEMBERS
from loader import dp


@dp.message_handler(isGroup(),Command('add_users'))
async def add_users(message: types.Message):
    try:
       await message.reply(f"Siz guruhga {ADD_MEMBERS[message.from_user.id]} ta odam qo'shgansiz")
    except:
        await message.reply(f"Siz guruhga 0 ta odam qo'shgansiz")
