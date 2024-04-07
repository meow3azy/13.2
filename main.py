class Category:
    def __init__(self, name, products):
        self.name = name
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    @property
    def товары(self):
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.products]

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.products)} шт."



class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def цена(self):
        return self.price

    @цена.setter
    def цена(self, new_price):
        if new_price <= 0:
            print("Цена введена некорректно")
        elif new_price < self.price:
            confirm = input("Цена товара понижается. Вы уверены? (y/n): ")
            if confirm.lower() == "y":
                self.price = new_price
                print("Цена товара успешно изменена")
            else:
                print("Действие отменено")
        else:
            self.price = new_price

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

