"""
Финансовый департамент корпорации "Цифровые Горизонты" зашифровал доступ к
квартальному отчету с помощью сложного протокола, основанного на API обмена
валют. Чтобы получить доступ, вам необходимо вычислить точный итоговый код.

По данным внутреннего аудита, код формируется путем суммирования результатов
множества стандартизированных обменных операций. Ваша задача —
автоматизировать этот процесс.

Что известно:
Целевой API: http://31.130.149.237/api/v1/ajax/GetSum
Логика API: Сервер принимает GET-запросы с параметрами GiveName, GetName,
Sum и Direction. В ответ он возвращает JSON с результатом обмена, включая поле
getSum , например: {"giveSum": 150.0, "getSum": 137.93}.

Данные для Операций:
Вам предоставлен словарь, определяющий стандартную сумму (amount) для
конвертации из каждой конкретной валюты (give):
amounts_per_give_currency = {
        "USD": 150, "EUR": 120, "RUB": 20000, "BYN": 50, "JPY": 50000,
        "GBP": 250, "CAD": 1000, "BTC": 0.01, "ETH": 0.5, "SOL": 10,
        "USDT": 150, "ADA": 300, "DOGE": 5000, "XRP": 1000, "BNB": 1,
        "USDC": 150, "TRX": 10000
}

Протокол расчета кода:
    1.  Для каждой валюты из словаря amounts_per_give_currency={...}
    необходимо выполнить операцию обмена на все остальные валюты из этого же
    списка (операция обмена валюты на саму себя не выполняется).
    2.  Сумма для каждой такой операции берется из словаря
    amounts_per_give_currency={...} в соответствии с валютой, которую вы
    отдаете GiveName.
    3.  Для каждой операции извлеките значение getSum из JSON-ответа.
    4.  Просуммируйте все эти числовые значения getSum.



Результат:
Итоговая сумма, округленная до двух знаков после запятой, и есть искомый код
доступа. Введите его в поле ниже в переменную key, чтобы разблокировать отчет.
Вставьте полученное значение в виде строки в поле ответа на Stepik

Технические подсказки:
Накапливайте сумму в переменной.
Округлите финальный результат с помощью round(float, 2).
Действуйте методично, и вы получите доступ к отчету!
"""

import requests

API_ENDPOINT = 'http://31.130.149.237/api/v1/ajax/GetSum'

amounts_per_give_currency = {
    "USD": 150, "EUR": 120, "RUB": 20000, "BYN": 50, "JPY": 50000,
    "GBP": 250, "CAD": 1000, "BTC": 0.01, "ETH": 0.5, "SOL": 10,
    "USDT": 150, "ADA": 300, "DOGE": 5000, "XRP": 1000, "BNB": 1,
    "USDC": 150, "TRX": 10000
}

total = 0
for give_currency in amounts_per_give_currency:
    total += sum(
        [
            requests.get(
                API_ENDPOINT,
                params={
                    'GiveName': give_currency,
                    'GetName': get_currency,
                    'Sum': amounts_per_give_currency[give_currency],
                    'Direction': 0
                }
            ).json()['getSum'] for get_currency in amounts_per_give_currency
            if get_currency != give_currency
        ]
    )

print(round(total, 2))
