import requests
from bs4 import BeautifulSoup

# Define the URL of the RoomRaccoon booking page
url = "https://booking.roomraccoon.us/demo-hotel-2362/en/?dateStart=2023-03-28&dateEnd=2023-03-29"

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html = response.content

# Use BeautifulSoup to parse the HTML content and extract the relevant div element
soup = BeautifulSoup(html, "html.parser")
booking_div = soup.find("div", {"class": "be-inner-container"})

# Write the HTML code for the div element and its children elements to a file
with open("booking.html", "w") as file:
    file.write(str(booking_div))
