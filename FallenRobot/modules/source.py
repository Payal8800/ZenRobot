from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from FallenRobot import pbot as client


ANON = "https://telegra.ph/file/4e097df12d8eb2ad48c81.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=ANON,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [ʀᴀᴅʜᴀ ✘ ʀᴏʙᴏᴛ-🇮🇳](t.me/RadhaXRobot_Bot)**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [𝐑ᴀᴅʜᴀ](t.me/MissRadha)
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

**ᴢᴇɴ ✘ ʀᴏʙᴏᴛ sᴏᴜʀᴄᴇ ɪs ᴘʀɪᴠᴀᴛᴇ 🥺 sᴏʀʀʏ ʙᴜᴛ ᴜ ᴄᴀɴ ᴜsᴇ ᴢᴇɴ ʀᴏʙᴏᴛ ғᴏʀ ɢʀᴏᴜᴘs.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("•👑 ᴏᴡɴᴇʀ ʟᴇɢᴇɴᴅ 👑•", url="https://t.me/MissRadha"
                    ),
                    InlineKeyboardButton(
                        "•💚sᴜᴘᴘᴏʀᴛ💚•",
                        url="https://t.me/RadhaSupport"
                    ),
                ],
                [
                    InlineKeyboardButton("• ➕ ᴀᴅᴅ ᴛᴏ ɢʀᴏᴜᴘ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ➕ •", url="https://t.me/RadhaXRobot_Bot?startgroup=true"),     
                ],
            ]
        ),
    )


__mod_name__ = "Rᴇᴩᴏ"

