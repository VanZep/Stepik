"""
Дополните приведенный ниже код так, чтобы в переменной result хранился словарь,
в котором для каждого символа строки text будет подсчитано количество его
вхождений.
"""

text = (
    'footballcyberpunkextraterritorialityconversationa'
    'listblockophthalmoscopicinterdependencemamauserfff'
)

result = {symbol: text.count(symbol) for symbol in set(text)}
print(result)
