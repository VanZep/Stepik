"""
Объявите класс Recipe для представления рецептов. Отдельные ингредиенты
рецепта должны определяться классом Ingredient. Объекты этих классов должны
создаваться командами:
ing = Ingredient(name, volume, measure)
recipe = Recipe()
recipe = Recipe(ing_1, ing_2,..., ing_N)
где ing_1, ing_2,..., ing_N - объекты класса Ingredient.

В каждом объекте класса Ingredient должны создаваться локальные атрибуты:
name - название ингредиента (строка)
volume - объем ингредиента в рецепте (вещественное число)
measure - единица измерения объема ингредиента (строка), например, литр,
чайная ложка, грамм, штук и т.д.

С объектами класса Ingredient должна работать функция:
str(ing)  # название: объем, ед. изм.
и возвращать строковое представление объекта в формате:
"название: объем, ед. изм."

Например:
ing = Ingredient("Соль", 1, "столовая ложка")
s = str(ing) # Соль: 1, столовая ложка

Класс Recipe должен иметь следующие методы:

add_ingredient(ing) - добавление нового ингредиента ing (объект класса
Ingredient) в рецепт (в конец)
remove_ingredient(ing) - удаление ингредиента по объекту ing (объект класса
Ingredient) из рецепта
get_ingredients() - получение кортежа из объектов класса Ingredient текущего
рецепта

Также с объектами класса Recipe должна поддерживаться функция:
len(recipe) - возвращает число ингредиентов в рецепте.

Пример использования классов (эти строчки в программе писать не нужно):
recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
n = len(recipe) # n = 3


P.S. На экран ничего выводить не нужно, только объявить классы.
"""


class Ingredient:
    name: str
    volume: (int, float)
    measure: str

    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __setattr__(self, key, value):
        if not isinstance(value, self.__annotations__[key]):
            raise TypeError(
                f'Значение {key} должно быть типом {self.__annotations__[key]}'
            )
        super().__setattr__(key, value)

    def __str__(self):
        return f'{self.name}: {self.volume}, {self.measure}'


class Recipe:

    def __init__(self, *args):
        self.ingredients = [ing for ing in args if isinstance(ing, Ingredient)]

    def add_ingredient(self, ing):
        if isinstance(ing, Ingredient):
            self.ingredients.append(ing)

    def remove_ingredient(self, ing):
        if ing in self.ingredients:
            self.ingredients.remove(ing)

    def get_ingredients(self):
        return tuple(self.ingredients)

    def __len__(self):
        return len(self.ingredients)


recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
# # print(*recipe.__dict__['ingredients'])
# ing = Ingredient("Мука", 1, "кг")
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
# recipe.add_ingredient(ing)
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
# recipe.remove_ingredient(ing)
ings = recipe.get_ingredients()
n = len(recipe)  # n = 3
print(n)
print(ings)
