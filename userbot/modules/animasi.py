from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")

# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Punten**")

# Create by myself @localheart


@register(outgoing=True, pattern='^.pantau(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Masih Ku Pantau**")


# Create by myself @localheart


@register(outgoing=True, pattern='^.idiot(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("\n╭╮╱╱╭╮"
                     "\n┃╰╮╭╯┃"
                     "\n╰╮╰╯╭┻━┳╮╭╮"
                     "\n╱╰╮╭┫╭╮┃┃┃┃"
                     "\n╱╱┃┃┃╰╯┃╰╯┃"
                     "\n╱╱╰╯╰━━┻━━╯"
                     "\nㅤㅤㅤ"
                     "\n╭━━━╮"
                     "\n┃╭━╮┃"
                     "\n┃┃╱┃┣━┳━━╮"
                     "\n┃╰━╯┃╭┫┃━┫"
                     "\n┃╭━╮┃┃┃┃━┫"
                     "\n╰╯╱╰┻╯╰━━╯"
                     "\nㅤㅤㅤ"
                     "\n╭━━━╮╱╭╮╱╱╱╭╮"
                     "\n┃╭━━╯╱┃┃╱╱╭╯╰╮"
                     "\n┃╰━━┳━╯┣┳━┻╮╭╯"
                     "\n┃╭━━┫╭╮┣┫╭╮┃┃"
                     "\n┃╰━━┫╰╯┃┃╰╯┃╰╮"
                     "\n╰━━━┻━━┻┻━━┻━╯"
                     "\nㅤㅤㅤ"
                     "\n╭━╮╱╭╮"
                     "\n┃┃╰╮┃┃"
                     "\n┃╭╮╰╯┣━━╮"
                     "\n┃┃╰╮┃┃╭╮┃"
                     "\n┃┃╱┃┃┃╰╯┃"
                     "\n╰╯╱╰━┻━━╯"
                     "\nㅤㅤㅤ"
                     "\n╭━━━╮╱╱╱╱╱╭╮╱╭╮"
                     "\n╰╮╭╮┃╱╱╱╱╱┃┃╭╯╰╮"
                     "\n╱┃┃┃┣━━┳╮╭┫╰┻╮╭╯"
                     "\n╱┃┃┃┃╭╮┃┃┃┃╭╮┃┃"
                     "\n╭╯╰╯┃╰╯┃╰╯┃╰╯┃╰╮"
                     "\n╰━━━┻━━┻━━┻━━┻━╯")

CMD_HELP.update({
    "sadboy":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.sadboy`\
    \n↳ : Biasalah sadboy hikss."
})

CMD_HELP.update({
    "punten":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.punten`\
    \n↳ : Cobain Ae."
})

CMD_HELP.update({
    "pantau":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.pantau`\
    \n↳ : Nyimak :v."
})

CMD_HELP.update({
    "idiot":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.idiot`\
    \n↳ : Lo idiot FIX."
})
