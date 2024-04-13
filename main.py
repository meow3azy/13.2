class Category:
    def __init__(self, name):
        self.__name = name
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    @property
    def products(self):
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]

    def __str__(self):
        return f"{self.__name}, количество продуктов: {len(self.__products)} шт."


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

    @staticmethod
    def create_product(name, price, quantity):
        return Product(name, price, quantity)

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."
