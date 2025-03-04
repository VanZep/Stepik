"""
Пользователь может ввести с клавиатуры следующие команды в виде строки:
top или Top или TOP
bottom или Bottom или BOTTOM
right или Right или RIGHT
left или Left или LEFT

cmd = input()

С помощью оператора match/case необходимо определить тип команды cmd и при
совпадении вывести на экран сообщение в формате:
Команда <название команды малыми буквами>

Например, при вводе Top, должны на выходе получить:
Команда top

И так для всех четырех команд. Если тип команды не определен, то вывести
строку:
Неверная команда

Sample Input:
BOTTOM

Sample Output:
Команда bottom
"""

cmd = input()

match cmd.lower():
    case 'top' | 'bottom' | 'right' | 'left' as command:
        print(f'Команда {command}')
    case _:
        print('Неверная команда')
