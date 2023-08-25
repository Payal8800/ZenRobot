
import asyncio
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message,
)


from FallenRobot import pbot as bot

Radha = "https://telegra.ph/file/4e097df12d8eb2ad48c81.jpg"


@bot.on_message(filters.command(["noob", "owner"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Zen,
        caption=f"""**ʜᴇʏ {message.from_user.mention()},\n\nɪ ᴀᴍ [「 ʀᴀᴅʜᴀ  ʀᴏʙᴏᴛ 」](t.me/RadhaXRobot_Bot)**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="https://t.me/MissRadha"),
                ]
            ]
        ),
    )


__mod_name__ = "Oᴡɴᴇʀ"
