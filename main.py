from bs4 import BeautifulSoup
import requests

def parse():
    proxies = {
        'http': 'http://proxy.omgtu:8080',
        'https': 'http://proxy.omgtu:8080'
    }
    url = 'https://omgtu.ru/general_information/faculties/'
    page = requests.get(url, proxies=proxies, verify=False)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")

    block = soup.find('div', class_='main__content')
    names = block.findAll('a')
    description = ''
    for data in names:
        name = data.find('span')
        name = data.text
        print(name)

parse()