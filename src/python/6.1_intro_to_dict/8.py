"""
Тестовый веб-сервер возвращает HTML-страницы по URL-адресам (строкам). На вход
программе поступают различные URL-адреса, записанные каждое с новой строки. В
программе уже реализовано считывание всех строк и сохранение их в виде списка:

lst_in = list(map(str.strip, sys.stdin.readlines()))
Необходимо перебрать в цикле этот список с URL-адресами и если адрес появился
(пришел) впервые, то на экране отобразить строку (без кавычек):

"HTML-страница для адреса <URL-адрес>"

и сохранить в словаре эту строку с ключом текущего URL-адреса. Если же
URL-адрес встречается (приходит) повторно (проверяется по ключам словаря),
то следует взять строку "HTML-страница для адреса <URL-адрес>" из этого
словаря и вывести на экран сообщение (без кавычек):

"Взято из кэша: HTML-страница для адреса <URL-адрес>"

Сообщения выводить каждое с новой строки.

P.S. Подобные задачи на практике решаются через хэш-таблицы. В Python словарь
- это хэш-таблица. Скорость поиска ключа в нем выполняется очень быстро
(намного быстрее, чем в списке). Именно поэтому решать ее через список
очень плохая практика.

Sample Input:
ustanovka-i-zapusk-yazyka
ustanovka-i-poryadok-raboty-pycharm
peremennyye-operator-prisvaivaniya-tipy-dannykh
arifmeticheskiye-operatsii
ustanovka-i-poryadok-raboty-pycharm

Sample Output:
HTML-страница для адреса ustanovka-i-zapusk-yazyka
HTML-страница для адреса ustanovka-i-poryadok-raboty-pycharm
HTML-страница для адреса peremennyye-operator-prisvaivaniya-tipy-dannykh
HTML-страница для адреса arifmeticheskiye-operatsii
Взято из кэша: HTML-страница для адреса ustanovka-i-poryadok-raboty-pycharm
"""

# import sys

# lst_in = list(map(int, sys.stdin.readlines()))
lst_in = [
    'ustanovka-i-zapusk-yazyka',
    'ustanovka-i-poryadok-raboty-pycharm',
    'peremennyye-operator-prisvaivaniya-tipy-dannykh',
    'arifmeticheskiye-operatsii',
    'ustanovka-i-poryadok-raboty-pycharm'
]


def func_1():
    """1-ое решение."""
    d = {}
    for url in lst_in:
        if url in d:
            print('Взято из кэша:', end=' ')
        else:
            d[url] = f'HTML-страница для адреса {url}'
        print(d[url])


def func_2():
    """2-ое решение."""
    d = {}
    for url in lst_in:
        if d.get(url):
            print('Взято из кэша:', end=' ')
        else:
            d[url] = f'HTML-страница для адреса {url}'
        print(d[url])


if __name__ == '__main__':
    func_1()
    print()
    func_2()
