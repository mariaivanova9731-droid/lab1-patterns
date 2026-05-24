class BaseModel:

    def to_dict(self):
        return self.__dict__

    def __repr__(self):

        attributes = []

        for key, value in self.__dict__.items():
            attributes.append(f"{key}={value}")

        attributes_str = ", ".join(attributes)

        return f"{self.__class__.__name__}({attributes_str})"


class User(BaseModel):

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Product(BaseModel):

    def __init__(self, title, price):
        self.title = title
        self.price = price


if __name__ == "__main__":

    user = User("Maria", 20)

    product = Product("Laptop", 1500)

    print(user)
    print(user.to_dict())

    print(product)
    print(product.to_dict())
