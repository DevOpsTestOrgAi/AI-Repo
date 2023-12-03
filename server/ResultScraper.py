from datetime import datetime
import requests
from bs4 import BeautifulSoup as Bs
import csv
import os
from flask import Response, jsonify

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
            return Response(status=500)  # Return an appropriate error status

        soup = Bs(response.text, 'html.parser')
        cards = soup.find_all('article', 'prd _fb col c-prd')

        cards__ = []
        for card in cards:
            record = get_record(card)
            cards__.append('jumia.ma' + record)
            print('jumia.ma' + record)

        return jsonify(cards__), 200
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return Response(status=500)  # Return an appropriate error status


# res(userInput)
