"""
Напишите код приложения на FastAPI, в котором асинхронная функция
list_cities() будет принимать GET запрос по маршруту /country/<country>,
получая строковой параметр country из параметра пути, а числовой параметр
limit из параметра запроса.

Конечная точка должна возвращать словарь с ключом country и значением
параметра country, и с ключом cities и значением в виде списка городов,
полученных из словаря country_dict для данной страны.

Количество городов в списке ответа должно быть ограничено параметром limit.

P.S. На экран ничего не нужно выводить, пример запроса:
/country/Russia?limit=3

ответ для него:
{'country': 'Russia', 'cities': ['Moscow', 'St. Petersburg', 'Novosibirsk']}

Пример словаря country_dict, глобальная переменная, добавлять в функцию
не нужно.

country_dict = {
    'Russia': [
        'Moscow', 'St. Petersburg', 'Novosibirsk', 'Ekaterinburg', 'Kazan'
    ],
    'USA': [
        'New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia'
    ],
    ...
}
"""

import uvicorn
from fastapi import FastAPI

country_dict = {
    'Russia': [
        'Moscow', 'St. Petersburg', 'Novosibirsk', 'Ekaterinburg', 'Kazan'
    ],
    'USA': [
        'New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia'
    ],
    'Germany': [
        'Berlin', 'Hamburg', 'Munich', 'Cologne', 'Frankfurt'
    ],
    'China': [
        'Chunzin', 'Shanghai', 'Beijing', 'Chenddu', 'Badodin'
    ],
    'Japan': [
        'Tokyo', 'Yokogama', 'Osaka', 'Nagoya', 'Sapporo'
    ],
}

app = FastAPI()


@app.get('/country/{country}')
async def list_cities(country: str, limit: int) -> dict:
    return {
        'country': country,
        'cities': country_dict[country][:limit]
    }


if __name__ == '__main__':
    uvicorn.run(app)
