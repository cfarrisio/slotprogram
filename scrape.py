import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.google.com/search?q=https%3A%2F%2Fhotels.cloudbeds.com%2Fen%2Freservation%2F&ei=mYgcZMWJB5Xe0PEPutia4Ac&hotel_occupancy=2&ved=0ahUKEwiFusmaxvL9AhUVLzQIHTqsBnwQ4dUDCBA&uact=5&oq=https%3A%2F%2Fhotels.cloudbeds.com%2Fen%2Freservation%2F&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzoICAAQgAQQ4wI6CwguEIAEEMcBEK8BOgUIABCABDoGCAAQFhAeSgQIQRgAUIYJWIYJYO0KaANwAXgAgAGPAYgBjwGSAQMwLjGYAQCgAQKgAQHAAQE&sclient=gws-wiz-serp#ip=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

hotels = []
for result in soup.select('.bkWMgd'):
    name = result.select_one('.dbg0pd').text
    address = result.select_one('.VkpGBb').text
    state = address.split(',')[-1].strip()
    try:
        room_count = int(result.select_one('.k7O2sd').text)
    except:
        room_count = None
    try:
        contact_person = result.select_one('.LrzXr').text
    except:
        contact_person = None
    try:
        phone_number = result.select_one('.LrzXr + .LrzXr').text
    except:
        phone_number = None
    try:
        email = result.select_one('.LrzXr + .LrzXr + .LrzXr').text
    except:
        email = None

    hotel_info = {
        'Hotel Name': name,
        'Address': address,
        'State': state,
        'Room Count': room_count,
        'Contact Person': contact_person,
        'Phone Number': phone_number,
        'Email': email
    }
    hotels.append(hotel_info)

df = pd.DataFrame(hotels)
print(df)
