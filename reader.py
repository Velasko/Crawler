import bs4 as bs
import urllib.request
import pickle

from sources import links, keywords

class Url():
    def __init__(self, url):
        self.text = url.text.lower()
        self.link = url.get('href')

    def __eq__(self, other):
        return( (self.link == other.link) and (self.text == other.text))

    def __repr__(self):
        return(self.text)

def found(link):
    texto = link.text
    for chave in keywords:
        if chave in texto:
            return(True)
    return(False)

def main():

    new = []

    with open('seen.pickle', 'rb') as file:
        seen = pickle.load(file)

    for link in links:
        sauce = urllib.request.urlopen(link).read()
        soup = bs.BeautifulSoup(sauce, 'lxml')

        for url in soup.find_all('a'):

            link = Url(url)

            if found(link) and  not link in seen:
                print(link.text)
                print(link.link)
                seen.append(link)
                new.append(link)

    with open('seen.pickle', 'wb') as file:
        pickle.dump(seen, file)

    return(new)
                
if __name__ == '__main__':
##    seen = []
##    with open('seen.pickle', 'wb') as file:
##        pickle.dump(seen, file)
    main()
