"""
Цель:
Посетить указанный веб-сайт, пройти по всем страницам в категории "мыши"
и из каждой карточки товара извлечь артикул. После чего все извлеченные
артикулы необходимо сложить и представить в виде одного числа.

Условия выполнения:
Посещение и анализ всех страниц в категории "МЫШИ" на веб-сайте
(всего 4 страницы).
Переход в каждую карточку товара на каждой странице категории "МЫШИ"
(всего 32 товара).
Используя библиотеку bs4, извлечение артикула из каждой карточки товара
(например, из элемента <p class="article">Артикул: 80244813</p>).
Сложение всех извлеченных артикулов.
Представление полученного результата в качестве ответа.
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://parsinger.ru/html/index3_page_4.html'
schema = 'https://parsinger.ru/html/'


def get_soup(html):
    return BeautifulSoup(html, 'html.parser')


def get_response(url):
    try:
        response = requests.get(url=url)
        response.raise_for_status()
        response.encoding = 'utf-8'

        return response.text
    except requests.RequestException as error:
        print(f"Произошла ошибка: {error}")


def get_pagination_links(html):
    soup = get_soup(html)
    pagination_tags = soup.find(class_='pagen').find_all('a')

    return [tag.get('href') for tag in pagination_tags]


def get_item_links(pagination_links):
    item_links = []
    for link in pagination_links:
        page_url = schema + link
        page_html = get_response(page_url)
        soup = get_soup(page_html)
        item_tags = soup.find_all(class_='name_item')
        links = [tag.get('href') for tag in item_tags]
        item_links.extend(links)

    return item_links


def get_articles(item_links):
    articles = []
    for link in item_links:
        item_url = schema + link
        item_html = get_response(item_url)
        soup = get_soup(item_html)
        article = int(soup.find('p', class_='article').text.split()[1])
        articles.append(article)

    return articles


def main():
    try:
        html = get_response(URL)
        pagination_links = get_pagination_links(html)
        item_links = get_item_links(pagination_links)
        articles = get_articles(item_links)
        print(sum(articles))

        return sum(articles)
    except Exception as error:
        print(f'Сбой в работе программы: {error}')


if __name__ == '__main__':
    main()
