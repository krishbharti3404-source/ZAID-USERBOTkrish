import asyncio
from collections import deque
from random import randint
from pyrogram import filters, Client
from pyrogram.types import Message
from Zaid.modules.help import add_command_help

# 🌈 Emoji animation sets
emojis = {
    "moon": list("🌗🌘🌑🌒🌓🌔🌕🌖"),
    "clock": list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"),
    "thunder": list("☀️🌤️⛅🌥️☁️🌩️🌧️⛈️⚡🌩️🌧️🌦️🌥️⛅🌤️☀️"),
    "earth": list("🌏🌍🌎🌎🌍🌏🌍🌎"),
    "heart": list("❤️🧡💛💚💙💜🖤🤍🤎"),
    
    # 💕 New aesthetic hearts
    "love": list("💞💓💗💖💘💝💟"),
    "sparkheart": list("❤️‍🔥💖❤️‍🔥💞💓💗"),
    "brokenheart": list("💔❤️‍🩹❤️💔❤️‍🩹❤️"),
    "beatingheart": list("💓💗💖💓💗💖💓💗💖"),
    "rainbowheart": list("❤️🧡💛💚💙💜🤎🖤🤍"),
    
    # 🌸 Extra visual cycles
    "flower": list("🌸🌺🌹🌷💐🌻🌼🌸"),
    "star": list("⭐🌟✨💫🌠"),
    "fire": list("🔥💥⚡💫🔥"),
    "sparkle": list("✨💫🌟💖🌠✨"),
}

emoji_commands = [x for x in emojis]


@Client.on_message(filters.command(emoji_commands, ".") & filters.me)
async def emoji_cycle(bot: Client, message: Message):
    deq = deque(emojis[message.command[0]])
    try:
        for _ in range(randint(16, 32)):
            await asyncio.sleep(0.3)
            await message.edit("".join(deq), parse_mode=None)
            deq.rotate(1)
    except Exception:
        await message.delete()


# 🎯 Special emoji senders
special_emojis_dict = {
    "target": {"emoji": "🎯", "help": "The special target emoji"},
    "dice": {"emoji": "🎲", "help": "The special dice emoji"},
    "bb": {"emoji": "🏀", "help": "The special basketball emoji"},
    "soccer": {"emoji": "⚽️", "help": "The special football emoji"},
}
special_emoji_commands = [x for x in special_emojis_dict]


@Client.on_message(filters.command(special_emoji_commands, ".") & filters.me)
async def special_emojis(bot: Client, message: Message):
    emoji = special_emojis_dict[message.command[0]]
    await message.delete()
    await bot.send_dice(message.chat.id, emoji["emoji"])


# 💡 Command help
special_emoji_help = [
    [".moon", "Cycles all the phases of the moon emojis."],
    [".clock", "Cycles all the phases of the clock emojis."],
    [".thunder", "Cycles thunder animations."],
    [".heart", "Cycles through heart emojis."],
    [".earth `or` .globe", "Make the world go round."],
    [".love", "Cycles romantic heart styles."],
    [".sparkheart", "Flaming or sparkling hearts."],
    [".brokenheart", "Animated heartbreak & healing."],
    [".beatingheart", "Beating heart animation."],
    [".rainbowheart", "Rainbow-themed hearts."],
    [".flower", "Cycle through beautiful flowers."],
    [".star", "Twinkling star animation."],
    [".fire", "Flame & energy cycle."],
    [".sparkle", "Shiny sparkle effect."],
]

for x in special_emojis_dict:
    special_emoji_help.append([f".{x}", special_emojis_dict[x]["help"]])

add_command_help("emoji", special_emoji_help)
