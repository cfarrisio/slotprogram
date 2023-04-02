from flask import Flask, render_template, request, redirect, url_for
import openai
import os
import random

app = Flask(__name__, template_folder='templates')

messages = []


# Define a list of welcome messages
welcome_messages = [
    "Hi, I'm Romy🦝 | What's on your mind?",
    "Hello, I'm Romy🦝 | What would you like to chat about today?",
    "Hey there, I'm Romy🦝 | How can I assist you?",
    "Greetings, I'm Romy🦝 | What brings you here?"
]

# Choose a random welcome message
welcome_message = random.choice(welcome_messages)

# Initialize the OpenAI API client
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_openai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=[" Human:", " AI:", "roomraccoon.com"]
    ).choices[0].text.strip()

    return response


def get_response(user_input):
    prompt = f"I need help with {user_input}."
    response = get_openai_response(prompt)

    return response


@app.route("/")
def home():
    global messages, welcome_message
    welcome_message = random.choice(welcome_messages)
    return render_template("index.html", welcome_message=welcome_message, messages=messages)


@app.route("/send_message", methods=["POST"])
def send_message():
    global messages
    user_input = request.form["user_input"]
    response = get_response(user_input)
    messages.append({"sender": "user", "text": user_input})
    messages.append({"sender": "bot", "text": response})
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run()
