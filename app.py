from flask import Flask, render_template, request
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

app = Flask(__name__, template_folder='templates')


def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt=prompt,
        temperature=0.69,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=[" Human:", " AI:"]
    )
    return response.choices[0].text.strip()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form["input"]
        rr_keywords = ["roomraccoon", "reservation system",
                       "booking engine", "property management system"]
        if any(keyword in user_input.lower() for keyword in rr_keywords):
            prompt = f"{start_sequence} {user_input} about Roomraccoon{restart_sequence}"
        else:
            prompt = f"{start_sequence} {user_input}{restart_sequence}"
        response = generate_response(prompt)
        return response
    return render_template("index.html")


@app.route('/process_input', methods=['POST'])
def process_input():
    user_input = request.form['input']
    response = generate_response(user_input)
    return response


if __name__ == "__main__":
    app.run(debug=True)
