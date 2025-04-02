"""
Объявите класс Money так, чтобы объекты этого класса можно было создавать
следующим образом:

my_money = Money(100)
your_money = Money(1000)

Здесь при создании объектов указывается количество денег, которое должно
сохраняться в локальном свойстве (атрибуте) money каждого экземпляра класса.
"""


class Money:

    def __init__(self, money):
        self.money = money


my_money = Money(100)
your_money = Money(1000)
print(my_money.money, your_money.money)
