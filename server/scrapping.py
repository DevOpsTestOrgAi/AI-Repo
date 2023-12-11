import csv
from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://www.jumia.ma/fashion-mode/'
driver = webdriver.Chrome()  # Assurez-vous d'avoir ChromeDriver installé et dans votre PATH
driver.get(url)

# Attendre que la page soit entièrement chargée (peut nécessiter des ajustements)
driver.implicitly_wait(10)

soup = BeautifulSoup(driver.page_source, 'html.parser')
category_list = soup.find('div', class_='flyout')


for item in category_list.find_all('a'):
        print(item)

   