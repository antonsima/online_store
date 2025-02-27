import json
import os

from config import JSON_DIR


class Product:
    """ Класс для представления продукта, который содержит имя, описание, цену и количество """

    name: str
    description: str
    __price: float
    quantity: int

    __products: list['Product'] = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """ Метод для инициализации экземпляра класса """

        is_created = False

        for existing_product in Product.products():
            if name == existing_product.name:
                existing_product.quantity += quantity
                if price > existing_product.price:
                    existing_product.price = price
                    self.name = name
                    self.description = description
                    self.__price = price
                    self.quantity = existing_product.quantity

                    is_created = True
                else:
                    self.name = name
                    self.description = description
                    self.__price = existing_product.price
                    self.quantity = existing_product.quantity

                    is_created = True

        if not is_created:
            self.name = name
            self.description = description
            self.__price = price
            self.quantity = quantity

            Product.products().append(self)


    @classmethod
    def products(cls):
        return cls.__products

    @classmethod
    def new_product(cls, name: str, description: str, price: float, quantity: int):
        for existing_product in cls.__products:
            if name == existing_product.name:
                existing_product.quantity += quantity
                if price > existing_product.price:
                    existing_product.price = price
                    return cls(name,
                               description,
                               price,
                               existing_product.quantity)
                else:
                    return cls(name,
                               description,
                               existing_product.price,
                               existing_product.quantity)

        cls.__products.append(Product(name, description, price, quantity))

        return cls(name,description,price,quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price > 0:
            if price < self.__price:
                is_stop = False

                while not is_stop:
                    answer = input('Цена, которую вы хотите установить, ниже существующей. Вы уверены?: y/n')
                    if answer == 'y':
                        self.__price = price
                        is_stop = True
                    elif answer == 'n':
                        print('Цена не изменена')
                        is_stop = True
                    else:
                        print('Введите один из предложенных вариантов: либо "y", либо "n"')
        else:
            print('Цена не должна быть нулевая или отрицательная')


class Category:
    """
    Класс для представления категории, который содержит имя, описание, продукты,
    количество категорий и количество продуктов
    """

    name: str
    description: str
    __products: list['Product']

    category_count = 0
    product_count = 0

    __categories: list['Category'] = []

    def __init__(self, name: str, description: str, products: list[Product]):
        """ Метод для инициализации экземпляра класса """

        tmp_old_category_names = []

        for existing_category in Category.categories():
            tmp_old_category_names.append(existing_category.name)

        for existing_category in Category.categories():
            if name == existing_category.name:
                tmp_old_product_names = []

                for existing_product in existing_category.products:
                    tmp_old_product_names.append(existing_product.name)

                for product in products:
                    if product.name in tmp_old_product_names:
                        for existing_product in existing_category.products:
                            if product.name == existing_product.name:
                                existing_product.quantity += product.quantity

                                if product.price > existing_product.price:
                                    existing_product.price = product.price
                    else:
                        existing_category.products.append(product)

                        Category.product_count += 1

                self.name = name
                self.description = description
                self.__products = existing_category.products

            else:
                if name not in tmp_old_category_names:
                    self.name = name
                    self.description = description
                    self.__products = products

                    Category.categories().append(self)

                    Category.category_count += 1
                    Category.product_count += len(products)

    @classmethod
    def categories(cls):
        return cls.__categories

    @property
    def products(self):
        [print(f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.') for product in
         self.__products]

        return self.__products

    def add_product(self, product: 'Product'):
        self.__products.append(product)


def get_categories_and_products_from_json_file(file_name: str) -> tuple[dict, dict]:
    """
    Принимает название файла в виде строки в директории json,
    возвращает кортеж словарей:
    tuple[0] = categories_obj
    tuple[1] = products_obj
    """

    with open(os.path.join(JSON_DIR, file_name), 'r', encoding='utf-8') as file:
        products = json.load(file)

    categories_obj = {}
    products_obj = {}

    for category in products:
        name = category['name']
        description = category['description']
        cat_products = category['products']

        categories_obj[name] = Category(name, description, cat_products)

        for product in cat_products:
            name = product['name']
            description = product['description']
            price = product['price']
            quantity = product['quantity']

            products_obj[name] = Product(name, description, price, quantity)
    return categories_obj, products_obj


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(category1.products)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)
