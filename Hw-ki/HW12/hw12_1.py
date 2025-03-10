"""1. Класс «Товар» содержит следующие закрытые поля:
● название товара
● название магазина, в котором подаётся товар
● стоимость товара в рублях
Класс «Склад» содержит закрытый массив товаров.
Обеспечить следующие возможности:
● вывод информации о товаре со склада по индексу
● вывод информации о товаре со склада по имени товара
● сортировка товаров по названию, по магазину и по цене
● перегруженная операция сложения товаров по цене"""


class Product:
    def __init__(self, name_prod, shop, price):
        self.name_prod = name_prod
        self.shop = shop
        self.price = price


    def __str__(self):
        return f'{self.name_prod} {self.shop} {self.price}'


    # def __add__(self, new):
    #     print("Присваивание")
    #     return Product(self.price + new)


class Store:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)


    def __getitem__(self, i):  # вывод информации о товаре со склада по индексу
        for i in self.products:
            return  self.products[i]


    def get_product_by_name(self, name):
        found_products = [product for product in self.products if product.name_prod.lower() == name.lower()]
        if found_products:
            for product in found_products:
                print(product)
        else:
            print("Товар с таким названием не найден.")


    def sort_by_name(self):
        self.products.sort(key=lambda product: product.name_prod)


    def sort_by_shop(self):
        self.products.sort(key=lambda product: product.shop)


    def sort_by_price(self):
        self.products.sort(key=lambda product: product.price)


    def show_all_products(self):
        for product in self.products:
            print(product)


    # def __add__(self, new):  # перегрузка цены не получилась (хотела добавить по Н рублей к цене каждого товара)
    #     for product in self.products:
    #         for j in product:
    #             return product[2] + new


store = Store()
product1 = Product ("Утюг", "Хоз.товары", 200)
store.add(product1)
store.add(Product("Телевизор", "Техника", 2000))
store.add(Product("Ноутбук", "Техника", 5000))
store.add(Product("Тостер", "Хоз.товары", 300))

print(store.products[2])

store.get_product_by_name("Утюг")
store.get_product_by_name("Холодильник")

print("\nСортировка товаров по имени:")
store.sort_by_name()
store.show_all_products()

print("\nСортировка товаров по цене:")
store.sort_by_price()
store.show_all_products()

print("\nСортировка товаров по магазину:")
store.sort_by_shop()
store.show_all_products()


# print(store.products + 20)  # должен быть вывод перегрузки цены