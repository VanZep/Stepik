"""
Объявите класс с именем Person и атрибутами:

name: 'Сергей Балакирев'
job: 'Программист'
city: 'Москва'

Создайте экземпляр p1 этого класса и проверьте, существует ли у него локальное
свойство с именем job. Выведите True, если оно присутствует в объекте p1 и
False - если отсутствует.
"""


class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'


p1 = Person()
print('job' in p1.__dict__)
