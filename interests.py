from bs4 import BeautifulSoup
import scholarly
import requests
from typing import *
import time
import json

def get_data(url: str) -> List[str]:
    result = []
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    names = soup.find('ul', {"class": "content"}).findAll('li')
    for name in names:
        result.append(name.find('a').text.split()[0] + ' ' +
                      name.find('a').text.split()[1])
    return result


def get_interests(names: List[str]) -> Dict:
    flag = False
    interests = {}
    counter = 0
    for name in names:
        if name == 'Остриков Александр':
            flag = True
        if not flag:
            continue

        counter += 1
        counter %= 10
        author = scholarly.search_author(name + ', ИТМО')
        print(name)
        try:
            author = next(author)
            interests.update({name:author.interests})
            print(author.interests)
            with open('interests3.txt', 'w') as f:
                f.write(str(interests))
                f.close()
        except:
            with open('interests3.txt', 'w') as f:
                f.write(str(interests))
                f.close()

    return interests


if __name__ == '__main__':

    interests = get_interests(get_data("http://edu.ifmo.ru/teachers/"))
