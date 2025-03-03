"""
Имеется следующий фрагмент программы с функцией parse_json и словарем
json_data:
def parse_json(data):
    match data:
        case {'id': ids, 'data': [_, {'login': login}, _, _]}:
            return ids, login

    return None


json_data = {
    'id': 2,
    'access': False,
    'data': [
        '26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4
    ]
}
С помощью оператора match/case в функцию parse_json добавьте в самое начало
шаблон для выделения значения ключа access с проверкой на тип bool и для
выделения даты (первое значение списка) из поля data с проверкой, что data
является списком. Возвратите выделенные два значения в виде кортежа в формате
(access, date).
"""


def parse_json(data):
    match data:
        case {'access': bool(access), 'data': list([date, *_])}:
            return access, date
        case {'id': ids, 'data': [_, {'login': login}, _, _]}:
            return ids, login

    return None


if __name__ == '__main__':
    json_data = {
        'id': 2,
        'access': False,
        'data': [
            '26.05.2023',
            {'login': '1234', 'email': 'xxx@mail.com'},
            2000,
            56.4
        ]
    }
    print(parse_json(json_data))
