import requests
from bs4 import BeautifulSoup
from time import sleep
import json

file_name = 'shop_by_parse.json'
data = {'planshety': []}
url = 'https://shop.by/planshety/'
page = 1


while True:
    r = requests.get(f'https://shop.by/planshety/?page_id={page}')
    # print(r.status_code)
    sleep(1)
    soup = BeautifulSoup(r.text, 'lxml')
    planshety = soup.find_all('div', class_='ModelList__ModelContentLine')
    #print(planshety)

    if len(planshety):
        for planshet in planshety:
            model = getattr(planshet.find('span', itemprop='name'), 'text', None)
            spans = planshet.find('span', class_='PriceBlock__PriceValue')
            price = ''

            if spans is not None:
                for span in spans.find_all('span'):
                    price += span.text.replace(' ', ' ')
            else:
                price = 'Нет в наличии'

            data['planshety'].append({'model': model, 'price': price})
        page += 1
        continue

    else:
        break

print(data)
with open(file_name, 'w', encoding='utf-8') as my_file:
    json.dump(data, my_file, indent=4, ensure_ascii=False)





