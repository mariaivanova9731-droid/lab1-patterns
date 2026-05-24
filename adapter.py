class OldPaymentSystem:

    def make_payment(self, value):
        print(f"Payment completed: {value}$")


class PaymentAdapter:

    def __init__(self, old_system):
        self.old_system = old_system

    def pay(self, amount):
        self.old_system.make_payment(amount)


if __name__ == "__main__":

    old_payment = OldPaymentSystem()

    adapter = PaymentAdapter(old_payment)

    adapter.pay(100)
