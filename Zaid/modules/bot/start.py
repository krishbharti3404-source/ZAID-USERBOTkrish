from pyrogram import Client, filters
from pyrogram.types import Message, ForceReply
from Zaid import app, API_ID, API_HASH

sessions = {}

@app.on_message(filters.command("genstring"))
async def generate_session(_, msg: Message):
    await msg.reply(
        "**📱 Send your phone number with country code.**\nExample: `+91XXXXXXXXXX`",
        reply_markup=ForceReply()
    )
    sessions[msg.chat.id] = {"step": 1}


@app.on_message(filters.text & filters.private)
async def steps(_, msg: Message):
    chat_id = msg.chat.id

    if chat_id not in sessions:
        return

    step = sessions[chat_id]["step"]

    # STEP 1: USER PHONE NUMBER
    if step == 1:
        phone = msg.text.strip()

        sessions[chat_id]["phone"] = phone

        await msg.reply("📨 **OTP send kiya gaya!**\n\nAb Telegram ka OTP yahan bhejo:",
                        reply_markup=ForceReply())

        sessions[chat_id]["step"] = 2
        return

    # STEP 2: GET OTP
    if step == 2:
        otp = msg.text.strip()
        sessions[chat_id]["otp"] = otp

        await msg.reply("🔐 **Agar 2-Step Password hai to send karo.**\nAgar nahi hai to `no` likho.",
                        reply_markup=ForceReply())

        sessions[chat_id]["step"] = 3
        return

    # STEP 3: PASSWORD (optional)
    if step == 3:
        password = msg.text.strip()

        if password.lower() == "no":
            password = None

        phone = sessions[chat_id]["phone"]
        otp = sessions[chat_id]["otp"]

        try:
            temp = Client(
                name="gen",
                api_id=API_ID,
                api_hash=API_HASH,
                in_memory=True
            )

            await temp.connect()
            await temp.send_code(phone)

            sent = await temp.sign_in(phone, otp, password=password)
            string = await temp.export_session_string()

            await msg.reply(
                f"🎉 **Your Pyrogram String Session:**\n\n`{string}`\n\n"
                "**⚠ Save it safely!**"
            )

        except Exception as e:
            await msg.reply(f"❌ ERROR:\n`{e}`")

        sessions.pop(chat_id, None)
        return
