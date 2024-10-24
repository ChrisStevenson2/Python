# Remember to install these libraries in python before building this
#
# pip install requests beautifulsoup4 pandas
#
#


import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website you want to scrape
url = 'https://www.etsy.com/shop/enchantedacresdesign'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the data you want to scrape (modify this according to the website's structure)
    data = []
    for item in soup.find_all('div', class_='item-class'):  # Adjust the tag and class
        title = item.find('h2').text  # Example of extracting a title
        description = item.find('p').text  # Example of extracting a description
        data.append({'Title': title, 'Description': description})
    
    # Create a DataFrame and save it to CSV
    df = pd.DataFrame(data)
    df.to_csv('output.csv', index=False)
    print('Data saved to output.csv')
else:
    print(f'Failed to retrieve data: {response.status_code}')
