import requests
from bs4 import BeautifulSoup as Bs

def get_url():
    url = "https://www.jumia.ma/smart-watch-t500-montre-intelligente-smart-watsh-full-appel-etanche-frequence-cardiaque-58887120.html"
    return url

def jumia(url):

    try:
        response = requests.get(url)
        print(response)
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
        soup = Bs(response.text, 'html.parser')
        wrapBody = soup.find('div', '-df -j-bet')
        cat = soup.find('div','brcbs col16 -pts -pbm')
        category = cat.a.findNext('a').findNext('a').findNext('a').text
        title = wrapBody.find('h1').text
        print(title)
        print(category)
        """save_file"""
        return { "errorMessage": "", "title": title, "category": category }

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return { "errorMessage": "Please recheck the url you passed and try again", "title": "", "category": "" }

