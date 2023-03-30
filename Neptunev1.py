import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

model_engine = "text-davinci-003"


def generate_response(prompt):
    response = openai.Completion.create(
        model=model_engine,
        prompt=prompt,
        temperature=0.69,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    return response.choices[0].text.strip()


print("Welcome to Neptune, your water navigation and outdoor expert AI assistant.")
while True:
    user_input = input("How can I assist you today?\nYou: ")
    prompt = f"Neptune: {user_input}\nMe:"
    response = generate_response(prompt)
    print(f"Neptune:{response}")
