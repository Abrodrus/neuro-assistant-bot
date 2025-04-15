import telebot
import openai
import os
from utils import load_prompt, generate_ai_response
from db import init_db

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY
system_prompt = load_prompt()

init_db()

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я твой нейропомощник. Просто напиши, что нужно сделать.")

@bot.message_handler(func=lambda m: True)
def handle_text(message):
    user_input = message.text
    response = generate_ai_response(system_prompt, user_input)
    bot.send_message(message.chat.id, response)

bot.polling()
