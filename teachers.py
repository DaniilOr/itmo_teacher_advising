import scholarly
import pandas
import transliterate
from typing import *

def get_listOfNames()-> List[List[str]]:
    data = pandas.read_csv('teachers.csv', sep = ';')
    listOfNames = []
    works = data['Выходные данные'].tolist()
    for work in works:
        names = work.split('//')[0].split('.,')[:-1]
        for i in range(len(names)):
            names[i] = names[i].strip()
            try:
                names[i] = names[i].split()[0] + ' ' + names[i].split()[1].split('.')[0]
            except:
                names[i] = ''
        if '.' in work.split('//')[0].split('.,')[-1]:
            names.append(work.split('//')[0].split('.,')[-1].split('.')[0])
        listOfNames.append(names)
    newListOfNames = []
    for names in listOfNames:
        newNames = []
        for name in names:
            new_name = name
            try:
                new_name = transliterate.translit(name, reversed = True)
            except:
                new_name = name
            finally:
                newNames.append(new_name)
        newListOfNames.append(newNames)
    return newListOfNames


def get_connections(authors: List[str], list: List[List[str]]) -> Dict:
    result = {}
    for i in range(len(list)):
        if not authors[i] in result.keys():
            authors[i] = authors[i].strip()
            try:
                authors[i] = authors[i].split()[0] + ' ' + authors[i].split()[1].split('.')[0]
            except:
                pass
            try:
                author_name = transliterate.translit(authors[i], reversed = True)
                authors[i] = author_name
            except:
                author_name = authors[i]
                authors[i] = author_name
            finally:
                result.update({author_name:set([authors[i]])})
        for name in list[i]:
            try:
                result[authors[i]].add(str(name.split()[0] + ' ' + name.split()[1].split('.')[0]).strip())
            except:
                result[authors[i]].add(name.strip())
    return result



if __name__ == '__main__':
    data = pandas.read_csv('teachers.csv', sep = ';')
    authors = data['Автор'].tolist()
    names = get_listOfNames()
    with open('names.txt', 'w') as f:
        f.write(str(names))
    connections = get_connections(authors, names)
    with open('connections.txt', 'w') as f:
        f.write(str(connections))
    print(str(connections))
