from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import isGroup
from data.config import MEMBER_ID,ADD_MEMBERS
from loader import dp,bot
from pprint import pprint
import json
@dp.message_handler(isGroup(),content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def new_member(message: types.Message):
    m1 = json.loads(message.as_json())

    if m1['from']['id'] not in MEMBER_ID:
        MEMBER_ID.append(m1['from']['id'])
        ADD_MEMBERS[m1['from']['id']] = 0
    if m1['from']['id'] in MEMBER_ID:
        ADD_MEMBERS[m1['from']['id']]+=len(m1['new_chat_members'])
    member = ",".join([m.get_mention(as_html=True) for m in message.new_chat_members])
    await message.reply(f"Xush kelibsiz, {member}")

@dp.message_handler(isGroup(),content_types=types.ContentTypes.LEFT_CHAT_MEMBER)
async def new_member(message: types.Message):
    if message.left_chat_member.id == message.from_user.id:
        await message.answer(f"{message.left_chat_member.get_mention(as_html=True)} guruhni tark etdi")
    elif message.from_user.id == (await bot.me).id:
        return
    else:
        await message.answer(f"{message.left_chat_member.get_mention(as_html=True)} guruhdan haydaldi"
                             f"Admin: {message.from_user.get_mention(as_html=True)}."
                             )



