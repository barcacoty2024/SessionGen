import asyncio
from telethon import Client
from pyrogram.types import Message
from pyrogram import Client, filters
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from pyrogram.errors import (
    ApiIdInvalid as ApiIdInvalid1,
    PhoneNumberInvalid as PhoneNumberInvalid1,
    PhoneCodeInvalid as PhoneCodeInvalid1,
    PhoneCodeExpired as PhoneCodeExpired1,
    SessionPasswordNeeded as SessionPasswordNeeded1,
    PasswordHashInvalid as PasswordHashInvalid1
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)


ask_ques = "<b>Lu pilih dah Nyet lu mau buat string apaan</b>"
buttons_ques = [
    [
        InlineKeyboardButton("Pyrogram v2", callback_data="pyrogram"),
        InlineKeyboardButton("Telethon", callback_data="telethon"),
    ],

]


@Client.on_message(filters.private & ~filters.forwarded & filters.command('generate'))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, is_bot: bool = False):
    if telethon:
        ty = "Telethon"
    else:
        ty = "Pyrogram"
        if not old_pyro:
            ty += " v2"
    if is_bot:
        ty += " Bot"
    user_id = msg.chat.id
    api_id = API_ID
    api_hash = API_HASH
    """
    if await cancelled(api_id):
        return
    try:
        api_id = int(api_id_msg.text)
    except ValueError:
        await api_id_msg.reply('Not a valid API_ID (which must be an integer). Please start generating session again.', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    api_hash_msg = await bot.ask(user_id, 'Please send your `API_HASH`', filters=filters.text)
    if await cancelled(salah):
        return
    api_hash = api_hash_msg.text
    """
    await asyncio.sleep(1.0)
    if not is_bot:
        t = "**Masukin dah tuh nomor tele lu pea.** \n**Contoh** : `+6214045` **Nah lu tungguin abis ntu**"
    else:
        t = "Now please send your `BOT_TOKEN` \nExample : `12345:abcdefghijklmnopqrstuvwxyz`'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("**Sabar ya lagi Ngirim OTP Ke Akun Lu...**")
    else:
        await msg.reply("**Sabar ya lagi OTP Ke Akun Lu...**")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id=api_id, api_hash=api_hash)
    elif telethon:
        client = TelegramClient(StringSession(), api_id=api_id, api_hash=api_hash)
    elif is_bot:
        client = Client(name=f"bot_{user_id}", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    else:
        client = Client(name=f"user_{user_id}", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    #except (ApiIdInvalid, ApiIdInvalidError):
        #await msg.reply('`API_ID` and `API_HASH` combination is invalid. Please start generating session again.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        #return
    except (PhoneNumberInvalid, PhoneNumberInvalidError):
        await msg.reply('**Nomer Akun Telegram Lu Ga Terdaftar Jink.**\n**Yang Bener Dikit Blog, Dari Ulang.**', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "**Lu periksa dah tuh OTP Di Akun Telegram Lu, Buru cepet kirim OTP ke sini.** \n **Cara Masukin OTP kek gini** `1 2 3 4 5`\n**Jangan Salah Ya Nyet.**", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply('**yah kelamaan kan pea...**', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError):
            await msg.reply('**Kode Nya Salah Monyet, Mata Lu Buta Apa Gimana.**', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError):
            await msg.reply('**Goblok, Dibilang Pake Spasi Tiap Kode.**', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError):
            try:
                two_step_msg = await bot.ask(user_id, '**Ribet di verif segala, Masukin Pw Akun lu buru.**', filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply('**Anjeng, Demen Banget Ngaret Jadi Manusia**', reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
            try:
                salah = await msg.reply("**Udah Jadi Nih Jing, Bentar**")
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled(salah):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError):
                await two_step_msg.reply('**Lu Pikun Apa Gimana Si Nyet, Password Sendiri Salah.**', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"**{ty.upper()} Nih String lu udeh jadi.** \n\n`{string_session}` \n\n**Minimal Bilang Makasih Ke** @mhmdwldnnnn **Atau Ke** @musik_supportdan **Karna Akun Lu Kaga Deak**"
    try:
        if not is_bot:
            await client.send_message("me", text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await client.disconnect()
    await asyncio.sleep(1.0)
    await bot.send_message(msg.chat.id, " {} **Dah Jadi tuh string lu.** \n\n**Cek Pesan Tersimpan Lu Yang Banyak Bokep Nya!** \n\n**Minimal Bilang Makasih Ke** @mhmdwldnnnn **Atau Ke** @musik_supportdan **Karna Akun Lu Kaga Deak**".format("telethon" if telethon else "pyrogram"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("Goblok Ga jelas !", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("Ngapain Jink !", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("Cancelled the generation process!", quote=True)
        return True
    else:
        return False
