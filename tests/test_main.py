from unittest.mock import patch

import pytest

from src.main import BaseProduct, Category, CategoryIter, Order, Product, get_categories_from_json_file


def test_product(test_product_watermelon):
    watermelon = test_product_watermelon
    assert watermelon.name == 'Арбуз'
    assert watermelon.description == 'Зеленый фрукт (или ягода)'
    assert watermelon.price == 100
    assert watermelon.quantity == 10


def test_category(test_category_fruits):
    fruits = test_category_fruits
    assert fruits.name == 'Фрукты'
    assert fruits.description == 'Сладкая, вкусная еда'

    assert fruits.products[0].name == 'Арбуз'
    assert fruits.products[0].description == 'Зеленый фрукт (или ягода)'
    assert fruits.products[0].price == 100

    fruits_again = test_category_fruits
    assert fruits_again.name == 'Фрукты'
    assert fruits_again.description == 'Сладкая, вкусная еда'

    assert fruits.products[0].name == 'Арбуз'
    assert fruits.products[0].description == 'Зеленый фрукт (или ягода)'
    assert fruits.products[0].price == 100

    assert fruits.products[0].quantity == 20


@patch('json.load')
def test_get_categories_from_json_file(mock_load, test_products_from_json):
    mock_load.return_value = test_products_from_json
    categories_obj = get_categories_from_json_file('products.json')

    assert categories_obj[0].name == 'Смартфоны'
    assert (categories_obj[0].description == 'Смартфоны, как средство не только коммуникации, '
                                             'но и получение дополнительных функций для удобства жизни')
    assert categories_obj[0].products[0].name == 'Samsung Galaxy C23 Ultra'
    assert categories_obj[0].products[0].description == '256GB, Серый цвет, 200MP камера'
    assert categories_obj[0].products[0].price == 180000.0
    assert categories_obj[0].products[0].quantity == 5

    assert categories_obj[0].products[1].name == 'Iphone 15'
    assert categories_obj[0].products[1].description == '512GB, Gray space'
    assert categories_obj[0].products[1].price == 210000.0
    assert categories_obj[0].products[1].quantity == 8

    assert categories_obj[0].products[2].name == 'Xiaomi Redmi Note 11'
    assert categories_obj[0].products[2].description == '1024GB, Синий'
    assert categories_obj[0].products[2].price == 31000.0
    assert categories_obj[0].products[2].quantity == 14

    assert categories_obj[1].name == 'Телевизоры'
    assert (categories_obj[1].description == 'Современный телевизор, который позволяет '
                                             'наслаждаться просмотром, станет вашим другом и помощником')

    assert categories_obj[1].products[0].name == '55" QLED 4K'
    assert categories_obj[1].products[0].description == 'Фоновая подсветка'
    assert categories_obj[1].products[0].price == 123000.0
    assert categories_obj[1].products[0].quantity == 7

    assert Category.category_count == 3
    assert Category.product_count == 7

    same_categories_obj = get_categories_from_json_file('products.json')

    assert same_categories_obj[0].name == 'Смартфоны'
    assert (same_categories_obj[0].description == 'Смартфоны, как средство не только коммуникации, '
                                                  'но и получение дополнительных функций для удобства жизни')
    assert same_categories_obj[0].products[0].name == 'Samsung Galaxy C23 Ultra'
    assert same_categories_obj[0].products[0].description == '256GB, Серый цвет, 200MP камера'
    assert same_categories_obj[0].products[0].price == 180000.0
    assert same_categories_obj[0].products[0].quantity == 10

    assert same_categories_obj[0].products[1].name == 'Iphone 15'
    assert same_categories_obj[0].products[1].description == '512GB, Gray space'
    assert same_categories_obj[0].products[1].price == 210000.0
    assert same_categories_obj[0].products[1].quantity == 16

    assert same_categories_obj[0].products[2].name == 'Xiaomi Redmi Note 11'
    assert same_categories_obj[0].products[2].description == '1024GB, Синий'
    assert same_categories_obj[0].products[2].price == 31000.0
    assert same_categories_obj[0].products[2].quantity == 28

    assert same_categories_obj[1].name == 'Телевизоры'
    assert (same_categories_obj[1].description == 'Современный телевизор, который позволяет '
                                                  'наслаждаться просмотром, станет вашим другом и помощником')

    assert same_categories_obj[1].products[0].name == '55" QLED 4K'
    assert same_categories_obj[1].products[0].description == 'Фоновая подсветка'
    assert same_categories_obj[1].products[0].price == 123000.0
    assert same_categories_obj[1].products[0].quantity == 14

    assert Category.category_count == 3
    assert Category.product_count == 7


def test_product_products(test_product_watermelon):
    assert test_product_watermelon.products()[0].name == 'Арбуз'
    assert test_product_watermelon.products()[0].description == 'Зеленый фрукт (или ягода)'
    assert test_product_watermelon.products()[0].price == 100
    assert test_product_watermelon.products()[0].quantity == 30


@patch('builtins.input')
def test_product_new_product_and_price_setter(mock_input):
    test_new_product = Product.new_product({'name': '55" QLED 4K',
                                            'description': 'Фоновая подсветка',
                                            'price': 123000.0,
                                            'quantity': 7})
    assert test_new_product.name == '55" QLED 4K'
    assert test_new_product.description == 'Фоновая подсветка'
    assert test_new_product.price == 123000.0
    assert test_new_product.quantity == 21

    mock_input.return_value = 'n'
    test_new_product.price = 1000
    assert test_new_product.price == 123000.0

    mock_input.return_value = 'y'
    test_new_product.price = 1000
    assert test_new_product.price == 1000

    mock_input.side_effect = [':)', 'y']
    test_new_product.price = 10
    assert test_new_product.price == 10

    test_new_product.price = -1
    assert test_new_product.price == 10


def test_init_existing_category_and_add_product(test_category_fruits, test_category_fruits_with_qiwi):
    first_init_category = test_category_fruits
    second_init_category = test_category_fruits_with_qiwi

    assert first_init_category.name == 'Фрукты'
    assert second_init_category.name == 'Фрукты'

    new_product = Product('Персик', 'Тоже вкусно', 100, 5)

    second_init_category.add_product(new_product)

    assert second_init_category.products[-1].name == 'Персик'


def test_category_categories(test_category_fruits_with_qiwi):
    assert test_category_fruits_with_qiwi.categories()[0].name == 'Фрукты'


def test_str_cat_and_prod(test_product_watermelon, test_category_fruits_with_qiwi):
    assert str(test_product_watermelon) == 'Арбуз, 100 руб. Остаток: 270 шт.'
    assert str(test_category_fruits_with_qiwi) == 'Фрукты, количество продуктов: 1195 шт.'


def test_add_products(test_product_watermelon, test_product_orange):
    watermelon = test_product_watermelon
    orange = test_product_orange

    total = watermelon + orange

    assert total == 86000


def test_category_iter(test_category_fruits_with_qiwi):
    tmp_test_list = []

    for product in CategoryIter(test_category_fruits_with_qiwi):
        tmp_test_list.append(str(product))

    assert tmp_test_list[0] == 'Арбуз, 100 руб. Остаток: 1120 шт.'
    assert tmp_test_list[1] == 'Апельсин, 100 руб. Остаток: 640 шт.'
    assert tmp_test_list[2] == 'Яблоко, 100 руб. Остаток: 620 шт.'
    assert tmp_test_list[3] == 'Киви, 100 руб. Остаток: 110 шт.'


def test_raises(test_smartphone, test_grass):
    smartphone = test_smartphone
    grass = test_grass

    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"

    assert grass.name == "Газонная трава"
    assert grass.description == "Элитная трава для газона"
    assert grass.price == 500.0
    assert grass.quantity == 20
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"

    smartphones = Category('Смартфоны', 'Для повседневной жизни', [smartphone])

    with pytest.raises(TypeError) as exc_info:
        smartphones.add_product('Строку нельзя добавить в категорию')

    assert str(exc_info.value) == "Нельзя добавить объект, не являющийся Product или его наследником"

    with pytest.raises(TypeError) as exc_info:
        smartphone + grass

    assert str(exc_info.value) == "Нельзя складывать отличающиеся экземпляры классов Product"

    with pytest.raises(ValueError) as exc_info:
        Product('name', 'description', 10, 0)

    assert str(exc_info.value) == "Нельзя создать товар с количеством равным нулю"


def test_base_product(mock_base_product):
    assert mock_base_product.price() == 'mocked price'
    assert mock_base_product.new_product() == 'mocked new_product'
    assert mock_base_product.products() == 'mocked products'


def test_base_product_error():
    with pytest.raises(TypeError) as exc_info:
        BaseProduct()

    assert (str(exc_info.value) == "Can't instantiate abstract class BaseProduct without "
                                   "an implementation for abstract methods 'new_product', 'price', 'products'")


def test_order(test_product_watermelon):
    order = Order(test_product_watermelon)

    assert order.name == 'Арбуз'
    assert order.quantity == 10
    assert order.total_cost == 1000

    assert str(order) == 'Арбуз, 10 шт., итоговая стоимость 1000 р.'


def test_category_middle_price():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])
    avg_price1 = category1.middle_price()

    category2 = Category("Холодильники", "Категория холодильников", [])
    avg_price2 = category2.middle_price()

    assert avg_price1 == 150250.0
    assert avg_price2 == 0
