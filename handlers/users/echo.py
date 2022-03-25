from aiogram import types
from filters import isPravite,isGroup
from loader import dp
from data.config import ADD_MEMBERS

# Echo bot
@dp.message_handler(isPravite(),state=None)
async def bot_echo(message: types.Message):
    #try:
     #   if int(ADD_MEMBERS[message.from_user.id])>1:
    await message.reply(message.text)
    #except:
     #   await message.reply(f"Siz guruhga odam qo'shing")

