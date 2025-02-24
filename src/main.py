import json
import os

from config import JSON_DIR


class Product:
    """ Класс для представления продукта, который содержит имя, описание, цену и количество """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
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

    category_quantity = 0
    products_quantity = 0

    def __init__(self, name, description, products):
        """ Метод для инициализации экземпляра класса """

        self.name = name
        self.description = description
        self.products = products

        Category.category_quantity += 1
        Category.products_quantity += len(products)


def read_json_file(file_name: str) -> list[dict]:
    """ Принимает название файла в виде строки в директории json """

    with open(os.path.join(JSON_DIR, file_name), 'r', encoding='utf-8') as file:
        products_json = json.load(file)

    products = json.loads(products_json)

    return products
