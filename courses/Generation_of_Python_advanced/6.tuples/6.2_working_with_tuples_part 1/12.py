"""
Дополните приведенный ниже код так, чтобы получить список, содержащий только
непустые кортежи исходного списка tuples, не меняя порядка их следования:
tuples = [
    (), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'),
    (1,), (), (), ('d',), ('', ''), ()
]
non_empty_tuples =

print(non_empty_tuples)
"""

tuples = [
    (), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'),
    (1,), (), (), ('d',), ('', ''), ()
]
non_empty_tuples_1 = list(filter(lambda x: len(x) != 0, tuples))
non_empty_tuples_2 = [element for element in tuples if element]

print(non_empty_tuples_1, non_empty_tuples_2, sep='\n')
