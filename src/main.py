import json
import os

from config import JSON_DIR


class Product:
    """ Класс для представления продукта, который содержит имя, описание, цену и количество """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """ Метод для инициализации экземпляра класса """

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """
    Класс для представления категории, который содержит имя, описание, продукты,
    количество категорий и количество продуктов
    """

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """ Метод для инициализации экземпляра класса """

        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)


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

        categories_obj[name] = Category(name, description, products)

        for product in cat_products:
            name = product['name']
            description = product['description']
            price = product['price']
            quantity = product['quantity']

            products_obj[name] = Product(name, description, price, quantity)
    return categories_obj, products_obj


if __name__ == "__main__":
    print(get_categories_and_products_from_json_file('products.json'))
    print(Category.category_count)
    print(Category.product_count)
