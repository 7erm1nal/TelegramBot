import asyncio
from telebot.async_telebot import AsyncTeleBot

with open('token.txt', 'r') as file:
    token=file.read()
bot = AsyncTeleBot(token)

@bot.message_handler(commands=['start', 'help'])
async def send_welcome(message):
    await bot.send_message(message.chat.id, "Привет!")




asyncio.run(bot.polling())