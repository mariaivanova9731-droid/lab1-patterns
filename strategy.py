from abc import ABC, abstractmethod


class DiscountStrategy(ABC):

    @abstractmethod
    def apply_discount(self, price):
        pass


class RegularDiscount(DiscountStrategy):

    def apply_discount(self, price):
        return price * 0.95


class VipDiscount(DiscountStrategy):

    def apply_discount(self, price):
        return price * 0.80


class HolidayDiscount(DiscountStrategy):

    def apply_discount(self, price):
        return price * 0.70


class ShoppingCart:

    def __init__(self, strategy):
        self.strategy = strategy

    def checkout(self, price):
        return self.strategy.apply_discount(price)


if __name__ == "__main__":

    price = 1000

    cart1 = ShoppingCart(RegularDiscount())
    print("Regular:", cart1.checkout(price))

    cart2 = ShoppingCart(VipDiscount())
    print("VIP:", cart2.checkout(price))

    cart3 = ShoppingCart(HolidayDiscount())
    print("Holiday:", cart3.checkout(price))
