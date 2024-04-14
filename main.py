class Category:
    def __init__(self, name):
        self.name = name
        self._products = []

    @property
    def products(self):
        return self._products

    def add_product(self, product):
        self._products.append(product)

    def __str__(self):
        return f"{self.name}: {', '.join(str(product) for product in self.products)}"

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена введена некорректно")
        elif new_price < self.__price:
            confirm = input("Цена товара понижается. Вы уверены? (y/n): ")
            if confirm.lower() == "y":
                self.__price = new_price
                print("Цена товара успешно изменена")
            else:
                print("Действие отменено")
        else:
            self.__price = new_price

    @classmethod
    def create_product(cls, **kwargs):
        return cls(**kwargs)

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."
