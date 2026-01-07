"""
В программе необходимо объявить классы для работы с кошельками в разных
валютах:
MoneyR - для рублевых кошельков
MoneyD - для долларовых кошельков
MoneyE - для евро-кошельков

Объекты этих классов могут создаваться командами:
rub = MoneyR() # с нулевым балансом
dl = MoneyD(1501.25) # с балансом в 1501.25 долларов
euro = MoneyE(100) # с балансом в 100 евро

В каждом объекте этих классов должны формироваться локальные атрибуты:
__cb - ссылка на класс CentralBank (центральный банк, изначально None)
__volume - объем денежных средств в кошельке (если не указано, то 0)

Также в классах MoneyR, MoneyD и MoneyE должны быть объекты-свойства (property)
для работы с локальными атрибутами:
cb - для изменения и считывания данных из переменной __cb
volume - для изменения и считывания данных из переменной __volume

Объекты классов должны поддерживать следующие операторы сравнения:
rub < dl
dl >= euro
euro > rub
rub == euro # значения сравниваются по текущему курсу центрального банка с
погрешностью 0.1 (плюс-минус)

При реализации операторов сравнения считываются соответствующие значения
__volume из сравниваемых объектов и приводятся к рублевому эквиваленту в
соответствии с курсом валют центрального банка.

Чтобы каждый объект классов MoneyR, MoneyD и MoneyE "знал" текущие котировки,
необходимо в программе объявить еще один класс CentralBank. Объекты класса
CentralBank создаваться не должны (запретить), при выполнении команды:
cb = CentralBank()
должно просто возвращаться значение None. А в самом классе должен
присутствовать атрибут:
rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

Здесь числа (в значениях словаря) - курс валюты по отношению к доллару.

Также в CentralBank должен быть метод уровня класса:
register(cls, money) - для регистрации объектов классов MoneyR, MoneyD и
MoneyE.

При регистрации значение __cb объекта money должно ссылаться на класс
CentralBank. Через эту переменную объект имеет возможность обращаться к
атрибуту rates класса CentralBank и брать нужные котировки.

Если кошелек не зарегистрирован, то при операциях сравнения должно
генерироваться исключение:
raise ValueError("Неизвестен курс валют.")

Пример использования классов (эти строчки в программе писать не нужно):
CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")

P.S. В программе на экран ничего выводить не нужно, только объявить классы.
"""

from __future__ import annotations


class CentralBank:
    rates: dict[str, float] = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs) -> None:
        return None

    @classmethod
    def register(cls, money: Money) -> None:
        money.cb = cls


class Money:
    __cb: CentralBank | None
    __volume: int | float

    def __init__(self, volume: int | float = 0) -> None:
        self.__cb = None
        self.__volume = volume

    @property
    def cb(self) -> CentralBank:
        return self.__cb

    @cb.setter
    def cb(self, cb: CentralBank) -> None:
        self.__cb = cb

    @property
    def volume(self) -> int | float:
        return self.__volume

    @volume.setter
    def volume(self, volume: int | float) -> None:
        self.__volume = volume

    def __eq__(self, other: Money) -> bool:
        self.check_register()
        other.check_register()
        return self.conversion_to_rubles() == other.conversion_to_rubles()

    def __lt__(self, other: Money) -> bool:
        self.check_register()
        other.check_register()
        return self.conversion_to_rubles() < other.conversion_to_rubles()

    def __le__(self, other: Money) -> bool:
        self.check_register()
        other.check_register()
        return self.conversion_to_rubles() <= other.conversion_to_rubles()

    def check_register(self) -> None:
        if self.cb is None:
            raise ValueError('Неизвестен курс валют.')


class MoneyR(Money):

    def conversion_to_rubles(self) -> float:
        return round(1.0 * self.volume, 1)


class MoneyD(Money):

    def conversion_to_rubles(self) -> float:
        return round(self.cb.rates.get('rub') * self.volume, 1)


class MoneyE(Money):

    def conversion_to_rubles(self) -> float:
        return round(self.cb.rates.get('rub') * self.volume, 1)


CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
print(CentralBank.rates)

cb1 = CentralBank()
print(cb1)

r = MoneyR(45000)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)
print(r.volume, r.cb.rates)
print(r.conversion_to_rubles(), d.conversion_to_rubles())

if r >= d:
    print("неплохо")
else:
    print("нужно поднажать")
