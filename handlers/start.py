from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>

**I am  Music Bot, an efficient and a perfect bot that lets you play music in your Telegram groups voice chat.**


__**Use the buttons below to know more about me.**__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒ COMMANDS ⚒", url="https://telegra.ph/VENOM-MUSIC-ROBOT-05-16"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔈 Channel", url="https://t.me/CrackMonkey"
                    ),
                    InlineKeyboardButton(
                        "Group 💬", url="https://t.me/CrackMonkeyChats"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Add Me To Your Group", url="http://t.me/VenomMusicBot?startgroup=true"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
