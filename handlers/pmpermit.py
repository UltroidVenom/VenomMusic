
from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hi there, This is the music assistant service of @VenomMusicBot .\n\n ❗️ Rules:\n   - No chatting allowed\n   - No spam allowed \n\n 👉 **IF YOU ARE UNABLE TO ADD ASSISTANT OR HAVE PROBLEM REGARDING MUSIC BOT KINDLY CONTACT @R2K_VENOM** \n\n **⚠️ Note : if you are unable to add music assistant in  private groups just make the group public for one minute and send the group link here or in @R2K_VENOM dm and after the music assistant joins you can make your group private again** \n\n **❗if you need any help just ask here @CrackMonkey**")
  return                        
