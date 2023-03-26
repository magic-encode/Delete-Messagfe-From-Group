import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types

from aiogram.dispatcher.filters import BoundFilter

API_TOKEN = '6282084971:AAFncZkeuxwzpiqJ7rzhLnpTEmgZAtk8o3A'

admin=5757658823

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



class IsGroup(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.chat.type in (
            types.ChatType.GROUP,
            types.ChatType.SUPERGROUP,
        )


class IsPrivate(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.PRIVATE


@dp.message_handler(IsPrivate(), commands=['start'])
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\nMeni guruhingizga qoshing va men guruhingizni kirdi-chiqdi \nhabarlarini o'chirib turaman.")


@dp.message_handler(IsGroup(), content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_member(message: types.Message):
    members = ", ".join([m.get_mention(as_html=True) for m in message.new_chat_members])
    out = await message.reply(f"{members} Muallima Bonu Guruhiga Xush kelibsiz.")
    await asyncio.sleep(15) 
    await message.delete()
    await out.delete()


@dp.message_handler(IsGroup(), content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def banned_member(message: types.Message):
    if message.left_chat_member.id == message.from_user.id:
        out = await message.answer(f"{message.left_chat_member.get_mention(as_html=True)} guruhni tark etdi")
        await asyncio.sleep(15)
        await message.delete()
        await out.delete()
        return
    else:
        out = await message.answer(f"{message.left_chat_member.full_name} guruhdan haydaldi "
                             f"Admin: {message.from_user.get_mention(as_html=True)}.")
        await asyncio.sleep(15)
        await message.delete()
        await out.delete()


async def on_startup_notify(dp: Dispatcher):
  
    try:
        await dp.bot.send_message(admin, "Bot ishga tushdi")

    except Exception as err:
        logging.exception(err)

async def on_startup(dispatcher):

    await on_startup_notify(dispatcher)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)