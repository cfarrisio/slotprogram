import requests

# Set the API endpoint URL
url = 'https://api.census.gov/data/2017/ecn/ecnhotel'

# Set any required parameters
params = {
    'get': 'GEO_ID,NAME,YEAR,ID,EMP,ESTAB',
    'for': 'state:*',
    'NAICS2017': '721110'
}

# Make a GET request to the API endpoint with the parameters
response = requests.get(url, params=params)

# Check if the response is successful (status code 200)
if response.status_code == 200:
    # Parse the JSON data from the response
    data = response.json()

    # Check if the 'results' key exists in the data dictionary
    if 'results' in data:
        # Loop through the results and print each item
        for result in data['results']:
            print(result)
    else:
        print('No results found.')
else:
    print('Error:', response.status_code)
