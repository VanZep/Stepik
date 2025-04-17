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


def get_links(selector_1, selector_2, *urls):
    with requests.Session() as session:
        links = []
        for url in urls:
            try:
                response = session.get(url=url, headers=get_headers())
                response.raise_for_status()
                response.encoding = 'utf-8'
                soup = get_soup(response.text)
                tags = soup.select_one(selector_1).select(selector_2)
                tag_links = [tag.get('href') for tag in tags]
                links.extend(tag_links)

            except requests.RequestException as error:
                print(f"Произошла ошибка: {error}")

    return links


def get_navigation_links(url):
    return get_links('.nav_menu', 'a', url)


def get_pagination_links(category_links):
    urls = (URL + link for link in category_links)
    return get_links('.pagen', 'a', *urls)


def get_item_links(pagination_links):
    urls = (URL + link for link in pagination_links)
    return get_links('*', '.name_item', *urls)


def get_total_price(item_links):
    with requests.Session() as session:
        total_price = 0
        for link in item_links:
            url = URL + link
            try:
                response = session.get(url=url, headers=get_headers())
                response.raise_for_status()
                response.encoding = 'utf-8'
                soup = get_soup(response.text)
                price = int(soup.find(id='price').text.split()[0])
                stock = int(soup.find(id='in_stock').text.split()[-1])
                total_price += price * stock

            except requests.RequestException as error:
                print(f"Произошла ошибка: {error}")

    return total_price


def main():
    try:
        category_links = get_navigation_links(START_URL)
        pagination_links = get_pagination_links(category_links)
        item_links = get_item_links(pagination_links)
        total_price = get_total_price(item_links)
        print(total_price)

    except Exception as error:
        print(f"Произошла ошибка: {error}")


if __name__ == '__main__':
    start_time = time.time()
    main()
    print(time.time() - start_time)
