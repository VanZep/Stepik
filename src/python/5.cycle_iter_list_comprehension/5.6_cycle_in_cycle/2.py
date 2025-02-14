"""
На вход программе подаются строки (URL-адреса, каждая с новой строки).
В программе уже реализовано их чтение и сохранение в списке:
lst_in = list(map(str.strip, sys.stdin.readlines()))

Требуется заменить в строках списка lst_in все пробелы на символ дефиса (-).
Следует учесть, что может быть несколько подряд идущих пробелов. Полученные
URL-адреса (строки) вывести на экран в столбик в порядке их следования в
списке lst_in.

Sample Input:
django chto  eto takoe    poryadok ustanovki
model mtv   marshrutizaciya funkcii  predstavleniya
marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya

Sample Output:
django-chto-eto-takoe-poryadok-ustanovki
model-mtv-marshrutizaciya-funkcii-predstavleniya
marshrutizaciya-obrabotka-isklyucheniy-zaprosov-perenapravleniya
"""

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

for i, s in enumerate(lst_in):
    while s.count('  '):
        s = s.replace('  ', ' ')
    s = s.replace(' ', '-')
    lst_in[i] = s
[print(i) for i in lst_in]
