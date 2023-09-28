import asyncio
from telebot import types
from telebot.async_telebot import AsyncTeleBot

with open('token.txt', 'r') as file:
    token=file.read()
bot = AsyncTeleBot(token)

@bot.message_handler(commands=['start'])
async def send_welcome(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(types.KeyboardButton("Меню"))
    await bot.send_message(message.chat.id, "Привет!", reply_markup=markup)

@bot.message_handler(func=lambda message:True)
async def Menu(message):
    if (message.text =="Меню"):
        markup = types.InlineKeyboardMarkup()
        btn_site=types.InlineKeyboardButton(text="Обо мне", url="https://github.com/7erm1naL/TelegramBot")
        btn_settings=types.InlineKeyboardButton(text="Настройки", callback_data='Settings')
        btn_subscribe=types.InlineKeyboardButton(text="Подписаться", callback_data='Subscribe')
        markup.add(btn_site, btn_settings, btn_subscribe)
        await bot.send_message(message.chat.id, text="Меню", reply_markup=markup)
    else:
        await bot.send_message(message.chat.id, "Чо говоришь? не понимаю")

@bot.callback_query_handler(func=lambda call: call.data=='Settings')
async def Settings(message):
    await bot.send_message(message.from_user.id, text="Настройки")

@bot.callback_query_handler(func=lambda call: call.data=='Subscribe')
async def Settings(message):
    await bot.send_message(message.from_user.id, text="Подписаться")

asyncio.run(bot.polling())