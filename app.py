from flask import Flask, render_template, request
import openai
import os
import random

openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

app = Flask(__name__, template_folder='templates')

# Define a list of messages
messages = [{'sender': 'bot', 'text': ''}]

# Define a list of welcome messages
welcome_messages = [
    "Hi, I'm Romy🦝 | What's on your mind?",
    "Hello, I'm Romy🦝 | What would you like to chat about today?",
    "Hey there, I'm Romy🦝 | How can I assist you?",
    "Greetings, I'm Romy🦝 | What brings you here?"
]

# Choose a random welcome message
welcome_message = random.choice(welcome_messages)


@app.route("/send_message", methods=["POST"])
def send_message():
    user_input = request.form.get("user_input")
    messages.append({'sender': 'user', 'text': user_input})

    rr_keywords = ["roomraccoon", "reservation system", "booking engine",
                   "property management system", "my account", "how do I"]
    if any(keyword in user_input.lower() for keyword in rr_keywords):
        if "how do I" in user_input.lower():
            response = "Sure! Here's how you can " + \
                user_input.lower().replace("how do I", "") + ": "
            response += "1. First, go to your Roomraccoon account. "
            response += "2. Next, navigate to the section where you can manage the settings or options you need to adjust. "
            response += "3. Finally, update your preferences and save your changes. That's it!"
        elif "adjust my rates" in user_input.lower():
            response = "To adjust your rates in your Roomraccoon account, please go to your Account Settings and click on the Rates tab. You can then adjust your rates using the slider below."
        else:
            prompt = f"{start_sequence} {user_input} about Roomraccoon{restart_sequence}"
            response = openai.Completion.create(
                engine="text-curie-001",
                prompt=prompt,
                temperature=0.69,
                max_tokens=1024,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                stop=[" Human:", " AI:"]
            ).choices[0].text.strip()

        # Append the user input and response to the messages list
        messages.append({'sender': 'user', 'text': user_input})
        messages.append({'sender': 'bot', 'text': response, 'response': ''})

        # Update the response in the messages list
        messages[-1]['response'] = response

    return render_template("index.html", response=response, messages=messages)


if __name__ == "__main__":
    print("Starting server...")
    app.run()
