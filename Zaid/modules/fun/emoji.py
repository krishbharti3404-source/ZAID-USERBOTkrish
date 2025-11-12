from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio


async def safe_edit(message: Message, text: str):
    """Safely edit the message only if changed"""
    try:
        if message.text != text:
            await message.edit_text(text)
    except Exception:
        pass


async def type_text(message: Message, text: str, delay: float = 0.15):
    """Letter-by-letter typing effect"""
    typed = ""
    for ch in text:
        typed += ch
        await safe_edit(message, typed)
        await asyncio.sleep(delay)


@Client.on_message(filters.command("love", ".") & filters.me)
async def love_animation(client: Client, message: Message):
    animations = ["❤️", "💞", "💓", "💗", "💖", "💘", "💕", "💝", "💟", "❤️‍🔥"]
    for emoji in animations:
        await safe_edit(message, emoji)
        await asyncio.sleep(0.3)
    await type_text(message, "I ❤️ YOU 😘")


@Client.on_message(filters.command("missyou", ".") & filters.me)
async def missyou_animation(client: Client, message: Message):
    animations = ["😔", "🥺", "💔", "😭", "💭", "🦋", "✨", "😞", "💌", "🤍"]
    for emoji in animations:
        await safe_edit(message, emoji)
        await asyncio.sleep(0.3)
    await type_text(message, "I MISS YOU 💔😔")


@Client.on_message(filters.command("happy", ".") & filters.me)
async def happy_animation(client: Client, message: Message):
    animations = ["😁", "😄", "😆", "😃", "😊", "😇", "🤗", "🥰", "✨", "💫"]
    for emoji in animations:
        await safe_edit(message, emoji)
        await asyncio.sleep(0.3)
    await type_text(message, "KEEP SMILING 😄💛")


@Client.on_message(filters.command("sad", ".") & filters.me)
async def sad_animation(client: Client, message: Message):
    animations = ["😢", "😭", "🥺", "💔", "😞", "😣", "😔", "😫", "😩", "💭"]
    for emoji in animations:
        await safe_edit(message, emoji)
        await asyncio.sleep(0.3)
    await type_text(message, "I'M JUST SAD 😢")


@Client.on_message(filters.command("butterfly", ".") & filters.me)
async def butterfly_animation(client: Client, message: Message):
    animations = ["🦋", "🌸", "💐", "🌷", "🌼", "🌻", "🌺", "🍃", "✨", "💫"]
    for emoji in animations:
        await safe_edit(message, emoji)
        await asyncio.sleep(0.3)
    await type_text(message, "FLY HIGH 🦋💖")


@Client.on_message(filters.command("sparkle", ".") & filters.me)
async def sparkle_animation(client: Client, message: Message):
    animations = ["✨", "💫", "🌟", "⚡", "🌠", "🌈", "💥", "🔥", "🌌", "⭐"]
    for emoji in animations:
        await safe_edit(message, emoji)
        await asyncio.sleep(0.3)
    await type_text(message, "SHINE BRIGHT ✨💫")


@Client.on_message(filters.command("heart", ".") & filters.me)
async def heart_animation(client: Client, message: Message):
    animations = ["❤️", "🧡", "💛", "💚", "💙", "💜", "🖤", "🤍", "🤎", "💖"]
    for emoji in animations:
        await safe_edit(message, emoji)
        await asyncio.sleep(0.3)
    await type_text(message, "HEARTS EVERYWHERE 💖")


@Client.on_message(filters.command("dream", ".") & filters.me)
async def dream_animation(client: Client, message: Message):
    animations = ["💭", "🌙", "⭐", "✨", "🌌", "🌠", "🌜", "🌛", "💫", "🌃"]
    for emoji in animations:
        await safe_edit(message, emoji)
        await asyncio.sleep(0.3)
    await type_text(message, "DREAM BIG 🌙💭")


# 🎂 HAPPY BIRTHDAY ANIMATION
@Client.on_message(filters.command("birthday", ".") & filters.me)
async def birthday_animation(client: Client, message: Message):
    args = message.text.split(maxsplit=1)
    name = args[1] if len(args) > 1 else "DEAR ❤️"

    animations = [
        "🎂", "🎈", "🎉", "🎊", "🎁", "🕯️", "🎂", "🎉", "💖", "✨",
        "🎂🎂", "🎈🎈", "🎊🎊", "🎁🎁", "💫", "🌸", "🦋", "💞", "💝"
    ]

    for emoji in animations:
        await safe_edit(message, emoji)
        await asyncio.sleep(0.3)

    text = f"HAPPY BIRTHDAY {name.upper()} 🎉🎂💖"
    await type_text(message, text)
