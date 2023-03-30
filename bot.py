import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "


def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=[" Human:", " AI:"]
    )
    return response.choices[0].text.strip()


print("Hi there, I'm Romy. Your AI assistant 🦝")
while True:
    user_input = input("You 👉 ")
    rr_keywords = ["roomraccoon", "reservation system",
                   "booking engine", "property management system"]
    if any(keyword in user_input.lower() for keyword in rr_keywords):
        prompt = f"{start_sequence} {user_input} about Roomraccoon{restart_sequence}"
    else:
        prompt = f"{start_sequence} {user_input}{restart_sequence}"
    response = generate_response(prompt)
    print(response)
    if "Goodbye" in response:
        break
