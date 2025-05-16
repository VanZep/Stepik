"""
Используя срезы, дополните приведенный ниже код так, чтобы он вывел все
элементы кортежа countries, кроме двух последних и трех первых:
countries = (
    'Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia',
    'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon'
)
"""

countries = (
    'Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia',
    'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon'
)

print(countries[3:-2])
