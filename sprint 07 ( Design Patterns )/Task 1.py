from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def cook(self):
        pass


class Factory(ABC):
    @abstractmethod
    def get_dish(self, type_of_meal):
        pass

class FactoryProducer():
    def get_factory(self,type_of_factory):
        if type_of_factory == 'italian':
            return ItalianDishesFactory()
        elif type_of_factory == 'french':
            return FrenchDishesFactory()

class ItalianDishesFactory(Factory):
    def get_dish(self, type_of_meal):
        if type_of_meal == 'main':
            return FettuccineAlfredo()
        elif type_of_meal == 'dessert':
            return Tiramisu()


class FrenchDishesFactory(Factory):
    def get_dish(self, type_of_meal):
        if type_of_meal == 'main':
            return DuckALOrange()
        elif type_of_meal == 'dessert':
            return CremeBrulee()


class FettuccineAlfredo(Product):
    def __init__(self):
        self.name = 'Fettuccine Alfredo'

    def cook(self):
        print(f'Italian main course prepared: {self.name}')


class Tiramisu(Product):
    def __init__(self):
        self.name = 'Tiramisu'

    def cook(self):
        print(f'Italian dessert prepared: {self.name}')


class DuckALOrange(Product):
    def __init__(self):
        self.name = "Duck À L'Orange"

    def cook(self):
        print(f'French main course prepared: {self.name}')


class CremeBrulee(Product):
    def __init__(self):
        self.name = 'Crème brûlée'

    def cook(self):
        print(f'French dessert prepared: {self.name}')

fp = FactoryProducer()
fac = fp.get_factory("italian")
main_dish = fac.get_dish("main")
main_dish.cook()
