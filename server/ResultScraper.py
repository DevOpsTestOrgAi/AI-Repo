from datetime import datetime
import requests
from bs4 import BeautifulSoup as Bs
import csv
import os

userInput = 'Knifes'


def get_url(userInput):
    template = "https://www.jumia.ma/catalog/?q={}"
    url = template.format(userInput)
    return url


def get_record(card):
    """extract data from a single record"""
    atag = card.a.get('href')
    return atag


def res(userInput):
    url = get_url(userInput)

    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
        soup = Bs(response.text, 'html.parser')
        cards = soup.find_all('article', 'prd _fb col c-prd')
        #with open(userInput + '.csv', 'w', newline='', encoding='utf-8-sig') as f:
        #    writer = csv.writer(f, delimiter=';')

            # Write the header row once
        #    writer.writerow(['Link'])

        #    for card in cards:
        #        record = get_record(card)
        #        writer.writerow(['jumia.ma'+record])
        #print(len(cards))  # check how many records are found
        #os.startfile(userInput+'.csv')  # for Windows

        for card in cards:
            record = get_record(card)
            print('jumia.ma'+record)
        print(len(cards))  # check how many records are found


    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


res(userInput)