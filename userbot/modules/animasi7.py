from time import sleep
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon import events
import asyncio


@register(outgoing=True, pattern="^.bang$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("DASAR KAU")
        sleep(2)
        await e.edit("BANGSAT")
        sleep(2)
        await e.edit("KONTOL")
        sleep(2)
        await e.edit("MEMEK")
        sleep(2)
        await e.edit("ANAK HARAM")
        sleep(2)
        await e.edit("ASU ASU ASU")
        sleep(2)
        await e.edit("MAMPUS KAU")
        sleep(2)
        await e.edit("MINTA DI ADOPSI")
        sleep(2)
        await e.edit("SAMA DAJAL")
        sleep(2)
        await e.edit("BIAR GUNA")
        sleep(2)
        await e.edit("DIKIT")
        sleep(2)
        await e.edit("DARI PADA")
        sleep(2)
        await e.edit("KAMU")
        sleep(2)
        await e.edit("SELAMANYA")
        sleep(2)
        await e.edit("JADI BEBAN")
        sleep(2)
        await e.edit("ORTU")
        sleep(1)
        await e.edit("KAMU")
        sleep(4)
        await e.delete()
        
@register(outgoing=True, pattern="^.tob$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
      await e.edit("WAHAY CUCUKU")
      sleep(1)
      await e.edit("IGATLAH")
      sleep(1)
      await e.edit("KAU DILAHIRKAN")
      sleep(1)
      await e.edit("BUKAN UNTUK")
      sleep(1)
      await e.edit("HANYA MAKAN SAJA")
      sleep(1)
      await e.edit("DAN MENJADI")
      sleep(1)
      await e.edit("BEBAN KELUARGA")
      sleep(4)
      await e.delete()

@register(outgoing=True, pattern='^.pyt(?: |$)(.*)')
async def typewriter(typew):
     typew.pattern_match.group(1)
     await typew.edit(
     "░░░░░░░░░░░░░░░░░░█░\n"
     "░░░█░░░░░░░░░░░░░██░\n"
     "░░██░░░░░░░░░░░████░\n"
     "░░███░░░░░░░░░██████\n"
     "░░█████░░░░░░█████●█\n"
     "░░░██████░░░███████░\n"
     "░░░░█████▓▓████████░\n"
     "░░░░░████▓▓████████░\n"
     "░░░░░░███▓▓███████░░\n"
     "░░░░░██▓▓██████░░░░░\n")
     await typew.edit(
     "░░░░░░░░░░░░░░░░░░█░\n"
     "░░░█░░░░░░░░░░░░░██░\n"
     "░░██░░░░░░░░░░░████░\n"
     "░░███░░░░░░░░░██████\n"
     "░░█████░░░░░░█████●█\n"
     "░░░██████░░░███████░\n"
     "░░░░█████▓▓████████░\n"
     "░░░░░████▓▓████████░\n"
     "░░░░░░███▓▓███████░░\n"
     "░░░░░██▓▓██████░░░░░\n"
     "░░░░██▓▓█████░░░░░░░\n"
     "░░░██▓▓████░░░░░░░░░\n"
     "░░██▓▓███░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n")
     await typew.edit(
     "░░░░░░░░░░░░░░░░░░█░\n"
     "░░░█░░░░░░░░░░░░░██░\n"
     "░░██░░░░░░░░░░░████░\n"
     "░░███░░░░░░░░░██████\n"
     "░░█████░░░░░░█████●█\n"
     "░░░██████░░░███████░\n"
     "░░░░█████▓▓████████░\n"
     "░░░░░████▓▓████████░\n"
     "░░░░░░███▓▓███████░░\n"
     "░░░░░██▓▓██████░░░░░\n"
     "░░░░██▓▓█████░░░░░░░\n"
     "░░░██▓▓████░░░░░░░░░\n"
     "░░██▓▓███░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░░░██▓▓██░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░██▓▓██░░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n")
     await typew.edit(
     "░░░░░░░░░░░░░░░░░░█░\n"
     "░░░█░░░░░░░░░░░░░██░\n"
     "░░██░░░░░░░░░░░████░\n"
     "░░███░░░░░░░░░██████\n"
     "░░█████░░░░░░█████●█\n"
     "░░░██████░░░███████░\n"
     "░░░░█████▓▓████████░\n"
     "░░░░░████▓▓████████░\n"
     "░░░░░░███▓▓███████░░\n"
     "░░░░░██▓▓██████░░░░░\n"
     "░░░░██▓▓█████░░░░░░░\n"
     "░░░██▓▓████░░░░░░░░░\n"
     "░░██▓▓███░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░░░██▓▓██░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░██▓▓██░░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░░░██▓▓██░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░██▓▓██░░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░░░██▓▓██░░░░░░░░░\n")
     await typew.edit(
     "░░░░░░░░░░░░░░░░░░█░\n"
     "░░░█░░░░░░░░░░░░░██░\n"
     "░░██░░░░░░░░░░░████░\n"
     "░░███░░░░░░░░░██████\n"
     "░░█████░░░░░░█████●█\n"
     "░░░██████░░░███████░\n"
     "░░░░█████▓▓████████░\n"
     "░░░░░████▓▓████████░\n"
     "░░░░░░███▓▓███████░░\n"
     "░░░░░██▓▓██████░░░░░\n"
     "░░░░██▓▓█████░░░░░░░\n"
     "░░░██▓▓████░░░░░░░░░\n"
     "░░██▓▓███░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░░░██▓▓██░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░██▓▓██░░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░░░██▓▓██░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░██▓▓██░░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░░░██▓▓██░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░██▓▓██░░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░░░██▓▓██░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n")
     await typew.edit(
     "░░░░░░░░░░░░░░░░░░█░\n"
     "░░░█░░░░░░░░░░░░░██░\n"
     "░░██░░░░░░░░░░░████░\n"
     "░░███░░░░░░░░░██████\n"
     "░░█████░░░░░░█████●█\n"
     "░░░██████░░░███████░\n"
     "░░░░█████▓▓████████░\n"
     "░░░░░████▓▓████████░\n"
     "░░░░░░███▓▓███████░░\n"
     "░░░░░██▓▓██████░░░░░\n"
     "░░░░██▓▓█████░░░░░░░\n"
     "░░░██▓▓████░░░░░░░░░\n"
     "░░██▓▓███░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░░░██▓▓██░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░██▓▓██░░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░░░██▓▓██░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░██▓▓██░░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░░░██▓▓██░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░██▓▓██░░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░░░██▓▓██░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░██▓▓██░░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░░░██▓▓██░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░██▓▓██░░░░░░░░░░░░░\n")
     await typew.edit(
     "░░░░░░░░░░░░░░░░░░█░\n"
     "░░░█░░░░░░░░░░░░░██░\n"
     "░░██░░░░░░░░░░░████░\n"
     "░░███░░░░░░░░░██████\n"
     "░░█████░░░░░░█████●█\n"
     "░░░██████░░░███████░\n"
     "░░░░█████▓▓████████░\n"
     "░░░░░████▓▓████████░\n"
     "░░░░░░███▓▓███████░░\n"
     "░░░░░██▓▓██████░░░░░\n"
     "░░░░██▓▓█████░░░░░░░\n"
     "░░░██▓▓████░░░░░░░░░\n"
     "░░██▓▓███░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░░░██▓▓██░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░██▓▓██░░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░░░██▓▓██░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░██▓▓██░░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░░░██▓▓██░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░██▓▓██░░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░░░██▓▓██░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░██▓▓██░░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░░░██▓▓██░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░██▓▓██░░░░░░░░░░░░░\n"
     "░░██▓▓██░░░░░░░░░░░░\n"
     "░░░██▓▓██░░░░░░░░░░░\n" 
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░░██▓▓██░░░░░░░░░░\n"
     "░░░░░██▓▓█░░░░░░░░░░\n"
     "░░░░░░█▓▓█░░░░░░░░░░\n"
     "░░░░░░░█▓█░░░░░░░░░░\n"
     "░░░░░░░░▓░░░░░░░░░░░\n")
     sleep(6)
     await typew.delete()
     
CMD_HELP.update({
    "bangsbat":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.bang`\
    \n↳ : Coba ae."
})

CMD_HELP.update({
    "tobat":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tob`\
    \n↳ : Coba ae."
})

CMD_HELP.update({
    "pythn":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.pyt`\
    \n↳ : Coba ae."
})
