import os
import openai
from telebot import TeleBot, types

# Загружаем токены
openai.api_key = os.getenv("OPENAI_API_KEY")
telegram_token = os.getenv("TELEGRAM_TOKEN")

bot = TeleBot(telegram_token)

# Загружаем prompt из файла
try:
    with open("prompt.txt", "r", encoding="utf-8") as f:
        system_prompt = f.read().strip()
except Exception as e:
    print(f"❌ Не удалось загрузить prompt.txt: {e}")
    system_prompt = "Ты нейроассистент. Отвечай кратко и по делу."

# Обработка команды /start
@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "Привет! Я твой нейропомощник. Просто напиши, что нужно сделать.")

# Обработка обычных сообщений
@bot.message_handler(func=lambda message: True)
def message_handler(message):
    try:
        user_text = message.text
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_text}
            ]
        )
        reply = response["choices"][0]["message"]["content"]
        bot.send_message(message.chat.id, reply)

    except Exception as e:
        print(f"❌ Ошибка OpenAI: {e}")
        bot.send_message(message.chat.id, "Извините, я не смог обработать ваш запрос. Попробуйте позже.")

# Запуск
if __name__ == "__main__":
    print("✅ Бот запущен")
    bot.polling(none_stop=True)
