from aiogram import types
import asyncio
from filters import IsGroup
from loader import dp


@dp.message_handler(IsGroup(), content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_member(message: types.Message):
    members = ", ".join([m.get_mention(as_html=True) for m in message.new_chat_members])
    out = await message.reply(f"{members} Muallima Bonu Guruhiga Xush kelibsiz.")
    try:
        await asyncio.sleep(15) 
        await message.delete()
        await out.delete()
    except:
        print("No message")


@dp.message_handler(IsGroup(), content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def banned_member(message: types.Message):

    if message.left_chat_member.id == message.from_user.id:
        out = await message.answer(f"{message.left_chat_member.get_mention(as_html=True)} guruhni tark etdi")
        try:
            await asyncio.sleep(15) 
            await message.delete()
            await out.delete()
            
        except:
            print("No message")
            
    else:
        out = await message.answer(f"{message.left_chat_member.full_name} guruhdan haydaldi "
                            f"Admin: {message.from_user.get_mention(as_html=True)}.")
        try:
            await asyncio.sleep(15) 
            await message.delete()
            await out.delete()
        except:
            print("No message")
