from abc import ABC, abstractmethod


class Coffee(ABC):

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass


class SimpleCoffee(Coffee):

    def cost(self):
        return 100

    def description(self):
        return "Simple coffee"


class CoffeeDecorator(Coffee):

    def __init__(self, coffee):
        self.coffee = coffee


class MilkDecorator(CoffeeDecorator):

    def cost(self):
        return self.coffee.cost() + 30

    def description(self):
        return self.coffee.description() + ", milk"


class CaramelDecorator(CoffeeDecorator):

    def cost(self):
        return self.coffee.cost() + 40

    def description(self):
        return self.coffee.description() + ", caramel"


if __name__ == "__main__":

    coffee = SimpleCoffee()

    print(coffee.description())
    print(coffee.cost())

    coffee = MilkDecorator(coffee)

    print(coffee.description())
    print(coffee.cost())

    coffee = CaramelDecorator(coffee)

    print(coffee.description())
    print(coffee.cost())
