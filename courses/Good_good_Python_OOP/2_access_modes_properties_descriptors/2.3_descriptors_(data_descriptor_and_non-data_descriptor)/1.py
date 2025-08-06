class StringField:
    def __set_name__(self, owner, name):
        print('__set_name__', name, owner.__name__, self.__dict__)
        self.name = "_" + name
        print(self.__dict__, self.__class__)

    def __get__(self, instance, owner):
        print('__get__')
        # return instance.__dict__[self.name]
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        print('__set__', instance.__class__, instance.__dict__, self.__class__, self.__dict__)
        # instance.__dict__[self.name] = value
        setattr(instance, self.name, value)
        print(instance.__dict__, value)


class DataBase:
    print('x = StringField()')
    x = StringField()
    # y = StringField()

    def __init__(self, x, y):
        print('self.x = x')
        self.x = x
        # self.y = y


db = DataBase('hi', 'low')
print(db.__dict__)
db.__dict__['x'] = 'top'
print(db.__dict__)
print(db.x)
# print(db.y)
