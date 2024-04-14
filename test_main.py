from main import Product, Category

if __name__ == "__main__":
    category = Category("Фрукты")
    print(category)
    products = [
        Product("Яблоки", 100, 10),
        Product("Груши", 200, 5),
        Product("Бананы", 150, 7),
        Product("Апельсины", 120, 8),
        Product("Мандарины", 300, 3)
    ]
    for product in products:
        category.add_product(product)
    print("Товары в категории:")
    for item in category.products:
        print(item)

    print("Товары до изменения цены:")
    for product in products:
        print(product)

    for product in products:
        product.price = 80

    print("Товары после изменения цены:")
    for product in products:
        print(product)
