import openai

def load_prompt():
    with open("prompt.txt", "r", encoding="utf-8") as f:
        return f.read()

def generate_ai_response(system_prompt, user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.5
        )
        return response.choices[0].message["content"]
    except Exception as e:
        print("Ошибка OpenAI:", e)
        return "Извините, я не смог обработать ваш запрос. Попробуйте позже."
