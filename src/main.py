import json
import os
from abc import ABC, abstractmethod
from typing import Iterator

from config import JSON_DIR


class BaseProduct(ABC):
    """ Абстрактный класс для Product """

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_dict: dict) -> 'Product':
        pass

    @classmethod
    @abstractmethod
    def products(cls) -> list['Product']:
        pass


class LogMixin:
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.__dict__})"


class Product(BaseProduct, LogMixin):
    """ Класс для представления продукта, который содержит имя, описание, цену и количество """

    name: str
    description: str
    __price: float
    quantity: int

    __products: list['Product'] = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """ Метод для инициализации экземпляра класса """

        tmp_existing_products_names = [existing_product.name for existing_product in Product.__products]

        if name not in tmp_existing_products_names:
            self.name = name
            self.description = description
            self.__price = price
            self.quantity = quantity

            Product.__products.append(self)
        else:
            for index, existing_product in enumerate(Product.__products):
                if name == existing_product.name:
                    existing_product.price = price
                    existing_product.quantity += quantity

                    self.self = existing_product

                    self.name = name
                    self.description = description
                    self.__price = existing_product.price
                    self.quantity = existing_product.quantity
                    break

        print(super().__repr__)

    def __str__(self) -> str:
        """
        Возвращает строку типа
        Название продукта, 80 руб. Остаток: 15 шт.
        """

        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other: 'Product') -> float:
        """ Возвращает стоимость двух объектов Product """

        if type(self) is type(other):
            return (self.__price * self.quantity) + (other.price * other.quantity)

        raise TypeError('Нельзя складывать отличающиеся экземпляры классов Product')

    @classmethod
    def products(cls) -> list['Product']:
        """ Возвращает список объектов Product """

        return cls.__products

    @classmethod
    def new_product(cls, product_dict: dict) -> 'Product':
        """ Возвращает новый объект Product """

        return cls(**product_dict)

    @property
    def price(self) -> float:
        """ Геттер для цены """

        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        """ Сеттер для цены """

        if price > 0:
            if price >= self.__price:
                self.__price = price
            else:
                is_stop = False

                while not is_stop:
                    answer = input('Цена, которую вы хотите установить, ниже существующей. Вы уверены? (y/n): ')
                    if answer == 'y':
                        self.__price = price
                        is_stop = True
                    elif answer == 'n':
                        print('Цена не изменена')
                        is_stop = True
                    else:
                        print('Введите один из предложенных вариантов: либо "y", либо "n": ')
        else:
            print('Цена не должна быть нулевая или отрицательная')


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)


class Category:
    """
    Класс для представления категории, который содержит имя, описание, продукты,
    количество категорий и количество продуктов
    """

    name: str
    description: str

    category_count = 0
    product_count = 0

    __categories: list['Category'] = []

    def __init__(self, name: str, description: str, products: list[Product]):
        """ Метод для инициализации экземпляра класса """

        tmp_old_category_names = [existing_category.name for existing_category in Category.__categories]

        if name not in tmp_old_category_names:
            self.name = name
            self.description = description
            self.__products = products
            Category.__categories.append(self)
            Category.category_count += 1
            Category.product_count += len(products)
        else:
            for cat_index, existing_category in enumerate(Category.__categories):
                if name == existing_category.name:
                    tmp_old_product_names = [existing_product.name for existing_product in
                                             existing_category.__products]

                    for prod_index, product_ in enumerate(products):
                        if product_.name in tmp_old_product_names:
                            old_prod_index = tmp_old_product_names.index(product_.name)

                            existing_category.__products[old_prod_index] = Product(products[prod_index].name,
                                                                                   products[prod_index].description,
                                                                                   products[prod_index].price,
                                                                                   products[prod_index].quantity,)

                        else:
                            existing_category.__products.append(product_)

                            Category.product_count += 1
                    self.self = existing_category

                    self.name = name
                    self.description = description
                    self.__products = existing_category.__products
                    break

    def __str__(self) -> str:
        """
        Возвращает строку типа
        Название категории, количество продуктов: 200 шт.
        """

        total_quantity = 0

        for existing_product in self.__products:
            total_quantity += existing_product.quantity

        return f'{self.name}, количество продуктов: {total_quantity} шт.'

    @classmethod
    def categories(cls) -> list['Category']:
        """ Возвращает список объектов Category """

        return cls.__categories

    @property
    def products(self) -> list['Product']:
        """ Возвращает список объектов Product, для объекта Category """

        [print(f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.') for product in
         self.__products]

        return self.__products

    def add_product(self, product: 'Product') -> None:
        """ Добавляет новый объект Product в категорию """

        if isinstance(product, Product):
            tmp_old_product_names = [existing_product.name for existing_product in self.__products]

            if product.name not in tmp_old_product_names:
                self.__products.append(product)

                Category.product_count += 1
        else:
            raise TypeError('Нельзя добавить объект, не являющийся Product или его наследником')


class CategoryIter:
    """ Создает итератор, возвращающий продукт из категории за одну итерацию """

    def __init__(self, category: 'Category'):
        """ Метод для инициализации экземпляра класса """

        self.category = category
        self.stop = 0

    def __iter__(self) -> Iterator['Product']:
        """ Метод для получения итератора для перебора объекта """

        self.products_quantity = len(self.category.products)
        return self

    def __next__(self) -> 'Product':
        """ Метод для перехода к следующему значению и его считыванию """

        if self.stop < self.products_quantity:
            self.stop += 1
            return self.category.products[self.stop - 1]
        else:
            raise StopIteration


def get_categories_from_json_file(file_name: str) -> list[Category]:
    """
    Принимает название файла в виде строки в директории json,
    возвращает список объектов категорий:
    """

    with open(os.path.join(JSON_DIR, file_name), 'r', encoding='utf-8') as file:
        products = json.load(file)

    categories_obj = []

    tmp_old_categories_names = [existing_category.name for existing_category in Category.categories()]
    tmp_old_product_names = [existing_product.name for existing_product in Product.products()]

    for category in products:
        cat_name = category['name']
        cat_description = category['description']
        cat_products = category['products']

        tmp_products_obj = []

        for product in cat_products:
            prod_name = product['name']
            prod_description = product['description']
            prod_price = product['price']
            prod_quantity = product['quantity']
            if prod_name in tmp_old_product_names:
                Product(prod_name, prod_description, prod_price, prod_quantity)
            else:
                tmp_products_obj.append(Product(prod_name, prod_description, prod_price, prod_quantity))
        if cat_name in tmp_old_categories_names:
            existing_category_index = tmp_old_categories_names.index(cat_name)
            categories_obj.append(Category.categories()[existing_category_index])
        else:
            categories_obj.append(Category(cat_name, cat_description, tmp_products_obj))

    return categories_obj
