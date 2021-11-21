import requests
from bs4 import BeautifulSoup
import pprint


res = requests.get(
    "https://www.kitchenstories.com/de/suche?search=schokoladenkuchen&type=recipe,article&orderBy=relevance&isCategory=false")
soup = BeautifulSoup(res.text, 'html.parser')
mama = soup.select('.site-grid')


def create_customer_fav(mama):

    my_dict = {}
    for i in mama:
        for a in i.find_all('a', href=True):
            wrd = ('https://www.kitchenstories.com'+a['href'])
            for b in i.select('.tile-like-button'):
                num = b.get_text().replace('k', '000').replace(',', '').replace('.', '')

                my_dict[wrd] = num
                sorted_dict = {}
                sorted_keys = sorted(
                    my_dict, key=my_dict.get, reverse=True)[:5]

                for w in sorted_keys:
                    sorted_dict[w] = my_dict[w]

    pprint.pprint(
        f'These are the top rated recepies for chocolate cake on https://www.kitchenstories.com/de:\n{sorted_dict}')


create_customer_fav(mama)


def create_customer_fast(mama):

    my_dict = {}
    for i in mama:
        for a in i.find_all('a', href=True):
            wrd = ('https://www.kitchenstories.com'+a['href'])
            for b in i.select('.archive-tile__prep-time'):
                num = b.get_text().replace(' Min.', '')

                my_dict[wrd] = num
                new_dict = sorted(my_dict, key=my_dict.get)[:5]
    pprint.pprint(
        f'These are the 5 fastest recepies for chocolate cake on https://www.kitchenstories.com/de:\n{new_dict}')


create_customer_fast(mama)
