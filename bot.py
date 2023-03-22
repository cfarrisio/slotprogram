import os
import openai

openai.api_key = os.getenv(
    "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")

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: what is the current weather in hamburg,mi?\n\nAI: The current weather in Hamburg, MI is sunny with a high of 66°F and a low of 55°F.\nHuman: thats incorrect\nAI: I apologize for the incorrect information. Would you like me to look for an alternative source of weather data?\nHuman: yes\nAI: Sure! I am now searching for the latest weather data for Hamburg, MI. Please hold while I look for reliable sources.\nHuman: okay\nAI: Based on my research, the current weather in Hamburg, MI is currently cloudy with a high of 61°F and a low of 44°F.\nHuman: whats the water temp in the huron river?\nAI: The current temperature in the Huron River is approximately 58-60 degrees Fahrenheit.\nHuman: I dont think thats accurate. Can you verify that?\nAI: I will be happy to verify the information. I am now searching for additional sources of data on the Huron River's water temperature. Please hold while I look for reliable sources.\nHuman: okay\nAI: According to my research, the current water temperature in the Huron River is between 56 and 61 degrees Fahrenheit.\nHuman: how many dams will I hit if I kayak from strawberry lake, hamburg mi, to downtown ann arbor using the huron river?\nAI: I am not sure of the exact number of dams you will encounter when kayaking from Strawberry Lake, Hamburg MI to downtown Ann Arbor. However, you should be aware that there are at least three dams located along the Huron River that you may encounter on your journey.\nHuman: what dams are those?\nAI: The three dams that are located along the Huron River are the Argo Dam, the Barton Dam, and the Geddes Dam.\nHuman: what about the flook dam near portage lake? Yes, the Flook Dam is also located near Portage Lake. It is located near the mouth of the Middle Huron River, near where it flows into Portage Lake.",
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
)
