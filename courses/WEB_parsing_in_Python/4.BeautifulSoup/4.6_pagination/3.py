"""
Цель:
Посетить указанный веб-сайт, систематически пройти по всем категориям,
страницам и карточкам товаров (всего 160 шт.). Из каждой карточки товара
извлечь стоимость и умножить ее на количество товара в наличии. Полученные
значения агрегировать для вычисления общей стоимости всех товаров на сайте.

Условия выполнения:
Посещение и анализ всех категорий, страниц и карточек товаров на веб-сайте
(всего 160 карточек товаров).
Из каждой карточки извлечение стоимости товара и его количества в наличии.
Умножение стоимости каждого товара на его количество в наличии.
Суммирование всех полученных значений для вычисления общей стоимости всех
товаров.
Представление итоговой общей стоимости в качестве ответа.
"""
import time

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

URL = 'https://parsinger.ru/html/'
START_URL = 'https://parsinger.ru/html/index1_page_1.html'

user_agent = UserAgent()


def get_headers():
    return {'User-Agent': user_agent.random}


def get_soup(html):
    return BeautifulSoup(html, 'html.parser')


def get_response(url):
    try:
        response = requests.get(url=url, headers=get_headers())
        response.raise_for_status()
        response.encoding = 'utf-8'

        return response.text
    except requests.RequestException as error:
        print(f"Произошла ошибка: {error}")


def get_navigation_links(url):
    html = get_response(url=url)
    soup = get_soup(html)
    link_tags = soup.find(class_='nav_menu').find_all('a')

    return [tag.get('href') for tag in link_tags]


def get_pagination_links(category_links):
    pagination_links = []
    for link in category_links:
        url = URL + link
        html = get_response(url=url)
        soup = get_soup(html)
        link_tags = soup.find(class_='pagen').find_all('a')
        links = [tag.get('href') for tag in link_tags]
        pagination_links.extend(links)

    return pagination_links


def get_item_links(pagination_links):
    item_links = []
    for link in pagination_links:
        url = URL + link
        html = get_response(url=url)
        soup = get_soup(html)
        link_tags = soup.find_all(class_='name_item')
        links = [tag.get('href') for tag in link_tags]
        item_links.extend(links)

    return item_links


def get_total_price(item_links):
    total_price = 0
    for link in item_links:
        url = URL + link
        html = get_response(url=url)
        soup = get_soup(html)
        price = int(soup.find(id='price').text.split()[0])
        stock = int(soup.find(id='in_stock').text.split()[-1])
        total_price += price * stock

    return total_price


def main():
    category_links = get_navigation_links(START_URL)
    pagination_links = get_pagination_links(category_links)
    item_links = get_item_links(pagination_links)
    total_price = get_total_price(item_links)
    print(total_price)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print(time.time() - start_time)
