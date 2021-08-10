# Zelda-Userbot


from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from userbot import CMD_HELP
from userbot.events import register


async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call))
    return xx.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]


@register(outgoing=True, pattern="^.startos(?: |$)(.*)", groups_only=True)
async def _(e):
    try:
        await e.client(startvc(e.chat_id))
        await e.edit("`Memulai Obrolan Suara...`")
    except Exception as ex:
        await e.edit(f"`{str(ex)}`")


@register(outgoing=True, pattern="^.stopos(?: |$)(.*)", groups_only=True)
async def _(e):
    try:
        await e.client(stopvc(await get_call(e)))
        await e.edit("`Menutup Obrolan Suara...`")
    except Exception as ex:
        await e.edit(f"`{str(ex)}`")


@register(outgoing=True, pattern="^.culikos(?: |$)(.*)", groups_only=True)
async def _(e):
    ok = await e.edit("`Mengundang Member Ke Obrolan Suara...`")
    users = []
    z = 0
    async for x in e.client.iter_participants(e.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await e.client(invitetovc(call=await get_call(e), users=p))
            z += 6
        except BaseException:
            pass
    await ok.edit(f"`Mengundang {z} Orang`")

CMD_HELP.update(
    {
        "os":
        "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.startos`\
         \n↳ : Memulai Obrolan Suara Dalam Grup. (Hanya Berlaku Untuk Admin Grup)\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.stopos`\
         \n↳ : Menutup Obrolan Suara Dalam Grup. (Hanya Berlaku Untuk Admin Grup)\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.culikos`\
         \n↳ : Mengundang Member Ke Obrolan Suara."
    }
)
