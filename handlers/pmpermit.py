
from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hi there, This is the music assistant service of @tgvc9robot .\n\n ❗️ Rules:\n   - No chatting allowed\n   - No spam allowed \n\n 👉 **SEND GROUP INVITE LINK HERE OF PUBLIC GROUPS IF YOU CANT ADD ASSISTANT** \n\n **⚠️ Note : if you are unable to add music assistant in  private groups just make the group public for one minute and send the group link here or in @God_loverr dm and after the music assistant joins you can make your group private again** \n\n **❗if you need any help just ask here @CheemsUserbot**")
  return                        
