# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.




from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hi there, This is a music assistant service of @tgvc8robot .\n\n **❗️⛔️ READ BEFORE TEXT ⛔️❗️**\n\n ❗️ Rules:\n   - No chatting allowed\n   - No spam allowed\n   - No Group links\n   - Don't msg hi hello to admins\n    - Don't send stickers\n\n ________________________________\n\n ⚡️𝐓𝐎 𝐀𝐃𝐃 𝐀𝐒𝐒𝐈𝐒𝐓𝐀𝐍𝐓 𝐌𝐀𝐍𝐔𝐀𝐋𝐋𝐘 𝐅𝐎𝐋𝐋𝐎𝐖 𝐁𝐄𝐋𝐎𝐖 𝐒𝐓𝐄𝐏𝐒:-\n\n add @tgvc8robot
Promote with all permissions\n\n Type /join\n\n ➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n👉 **SEND YOUR GROUP USERNAMES ONLY‼️.**\n\n  **⚠️ Note : if you are unable to add music assistant in  private groups just make the group public for one minute and send the group link here or in @God_loverr dm and after the music assistant joins you can make your group private again.**\n\n **🔴 DONT MSG HI HELLO TO @GOD_LOVERR JUST MSG YOUR GROUP USERNAME AND WAIT FOR HIS REPLY AND DONT SPAM.**\n\n   **❗if you need any help just ask here @CheemsUserbot**\n\n")
  return                        
