from userbot import CMD_HELP
from userbot.events import register
from telethon.tl import functions
from telethon.tl.functions.messages import GetFullChatRequest
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError)
from telethon.tl.functions.channels import GetFullChannelRequest


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except BaseException:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Channel Atau Super Group Tidak Ditemukan.`")
            return None
        except ChannelPrivateError:
            await event.reply("`Tidak Bisa Menambahkan Ke Group`")
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel Atau Super Group Tidak Ditemukan.`")
            return None
        except (TypeError, ValueError) as err:
            await event.reply("`Channel Atau Super Group Tidak Ditemukan.`")
            return None
    return chat_info


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = ' '.join(names)
    return full_name


@register(outgoing=True, pattern="^.culikall ?(.*)")
async def get_users(event):
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        hell = await event.reply("`Memulai Penculikan...`")
    else:
        hell = await event.edit("`Memproses Penculikan...`")
    legendx22 = await get_chatinfo(event)
    chat = await event.get_chat()
    if event.is_private:
        return await hell.edit("`Maaf Lord, gabisa nyulik disini..`")
    s = 0
    f = 0
    error = 'None'

    await hell.edit("**Terminal Status**\n\n`Mamuat Users.......`")
    async for user in event.client.iter_participants(legendx22.full_chat.id):
        try:
            if error.startswith("Too"):
                return await hell.edit(f"**Terjadi Kesalahan...**\n(`Mungkin saat ini Lord sedang Limit, coba lagi nanti`)\n⛔ **Kesalahan** : \n`{error}`\n\n✅ Terculik `{s}` Orang \n❎ Gagal Nyulik `{f}` Orang")
            await event.client(functions.channels.InviteToChannelRequest(channel=chat, users=[user.id]))
            s = s + 1
            await hell.edit(f"**Proses Berjalan...**\n\n✅ Terculik `{s}` Orang \n❎ Gagal Nyulik `{f}` Orang\n\n⛔ **Kesalahan :** `{error}`")
        except Exception as e:
            error = str(e)
            f = f + 1
    return await hell.edit(f"**Proses Selesai** \n\n✅ Terculik `{s}` Orang \n❎ Gagal Nyulik `{f}` Orang")


CMD_HELP.update(
    {
        "culik": """**Plugin : **`culik`
  •  **Syntax : **`.culik <username>`
  •  **Function : **__Culik Orang ke Group Chat__
  •  **Syntax : **`.culikall <groupid>`
  •  **Function : **__Culik semua member GC ke GC mu__
"""
    }
)
