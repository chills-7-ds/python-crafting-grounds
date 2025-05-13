import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.find_all('div', class_='quote')

for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    tags = [tag.text for tag in quote.find_all('a', class_='tag')]

    print(f'Quote  : {text}')
    print(f'Author : {author}')
    print(f'Tags   : {", ".join(tags)}')
    print('-' * 80)
