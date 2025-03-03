from unittest.mock import patch

from src.main import Category, Product, get_categories_from_json_file


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
