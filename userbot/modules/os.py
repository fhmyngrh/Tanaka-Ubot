# Zelda-Userbot


from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from userbot import CMD_HELP
from userbot import ALIVE_NAME
from userbot.events import register


async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call))
    return xx.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


@register(outgoing=True, pattern="^.startos(?: |$)(.*)", groups_only=True)
async def start_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await c.edit(f"**Maaf {ALIVE_NAME} Bukan Admin. Tidak bisa memulai Obrolan Video**")
        return
    try:
        await c.client(startvc(c.chat_id))
        await c.edit("`Voice Chat Started...`")
    except Exception as ex:
        await c.edit(f"**ERROR:** `{ex}`")
        
@register(outgoing=True, pattern="^.ostitle(?: |$)(.*)", groups_only=True)
async def change_title(e):
    title = e.pattern_match.group(1)
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not title:
        return await e.edit("**Silahkan Masukan Title Obrolan Suara Grup**")

    if not admin and not creator:
        await e.edit(f"**Maaf {ALIVE_NAME} Bukan Admin. Tidak bisa mengganti judul Obrolan Video**")
        return
    try:
        await e.client(settitle(call=await get_call(e), title=title.strip()))
        await e.edit(f"**Berhasil Mengubah Judul VCG Menjadi** `{title}`")
    except Exception as ex:
        await e.edit(f"**ERROR:** `{ex}`")


@register(outgoing=True, pattern="^.stopos(?: |$)(.*)", groups_only=True)
async def stop_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await c.edit(f"**Maaf {ALIVE_NAME} Bukan Admin. Tidak bisa menutup Obrolan Video**")
        return
    try:
        await c.client(stopvc(await get_call(c)))
        await c.edit("`Voice Chat Stopped...`")
    except Exception as ex:
        await c.edit(f"**ERROR:** `{ex}`")


@register(outgoing=True, pattern="^.culikos(?: |$)(.*)", groups_only=True)
async def _(c):
    await c.edit("`Inviting Members to Voice Chat...`")
    users = []
    z = 0
    async for x in c.client.iter_participants(c.chat_id):
        if not x.bot:
            users.append(x.id)
    botman = list(user_list(users, 6))
    for p in botman:
        try:
            await c.client(invitetovc(call=await get_call(c), users=p))
            z += 6
        except BaseException:
            pass
    await c.edit(f"`{z}` **Orang Berhasil diundang ke VCG**")

CMD_HELP.update(
    {
        "os":
        "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.startos`\
         \n↳ : Memulai Obrolan Suara Dalam Grup. (Hanya Berlaku Untuk Admin Grup)\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.stopos`\
         \n↳ : Menutup Obrolan Suara Dalam Grup. (Hanya Berlaku Untuk Admin Grup)\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ostitle`\
         \n↳ : Mengubah title/judul voice chat group.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.culikos`\
         \n↳ : Mengundang Member Ke Obrolan Suara."
    }
)
