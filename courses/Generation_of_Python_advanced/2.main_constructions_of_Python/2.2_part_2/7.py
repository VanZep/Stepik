"""
Тимур и Руслан пытаются разделить фронт работы по курсу "Python для
профессионалов". Для этого они решили сыграть в камень, ножницы и бумагу.
Помогите ребятам бросить честный жребий и определить, кто будет делать
очередной модуль нового курса.

Формат входных данных
На вход программе подаются две строки текста, содержащие слова "камень",
"ножницы" или "бумага". На первой строке записан выбор Тимура, на второй –
выбор Руслана.

Формат выходных данных
Программа должна вывести результат жеребьевки, то есть кто победит: Тимур,
Руслан или же они сыграют вничью.

Примечание. Правила игры стандартные: камень побеждает ножницы, но проигрывает
бумаге, а ножницы побеждают бумагу.

Тестовые данные

Sample Input 1:
камень
бумага

Sample Output 1:
Руслан

Sample Input 2:
камень
камень

Sample Output 2:
ничья

Sample Input 3:
камень
ножницы

Sample Output 3:
Тимур
"""


def func_1():
    """1-ое решение."""
    timur_victory_conditions = (
        'каменьножницы', 'ножницыбумага', 'бумагакамень'
    )
    timur_choiсe = input()
    ruslan_choice = input()

    if timur_choiсe + ruslan_choice in timur_victory_conditions:
        print('Тимур')
    elif timur_choiсe == ruslan_choice:
        print('ничья')
    else:
        print('Руслан')


def func_2():
    """2-ое решение."""
    choices = ('камень', 'ножницы', 'бумага')
    results = ('ничья', 'Руслан', 'Тимур')
    timur_choice = input()
    ruslan_choice = input()
    difference = choices.index(timur_choice) - choices.index(ruslan_choice)
    result = results[difference]
    print(result)


if __name__ == '__main__':
    func_1()
    func_2()
