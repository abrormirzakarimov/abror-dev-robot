import io
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from filters import isGroup,AdminFilter

from loader import dp,bot

@dp.message_handler(isGroup(),Command('set_photo',prefixes='!/'),AdminFilter())
async def set_photo(message: types.Message):
    sourse_message = message.reply_to_message
    photo = sourse_message.photo[-1]
    photo = await photo.download(destination=io.BytesIO())
    input_file = types.InputFile(photo)
    await message.chat.set_photo(photo=input_file)

@dp.message_handler(isGroup(),Command('set_title',prefixes='!/'),AdminFilter())
async def set_title(message: types.Message):
    sourse_message = message.reply_to_message
    title = sourse_message.text
    await bot.set_chat_title(message.chat.id, title=title)

@dp.message_handler(isGroup(),Command('set_description',prefixes='!/'),AdminFilter())
async def set_description(message: types.Message):
    sourse_message = message.reply_to_message
    description = sourse_message.text
    await message.chat.set_description(description=description)