import requests
from bs4 import BeautifulSoup


# Build a web crawler

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://bikroy.com/bn/ads/dhaka?page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.find_all('a', {'class':'item-title h4'}):
            href = "https://bikroy.com" + link.get('href')
            title = link.string
            print(href)
            print(title)
            get_single_item_data(href)
        page += 1

 #single Data item

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.find_all('span', {'class': 'date'}):
        print('Time and Date: ' + item_name.string)



trade_spider(1)