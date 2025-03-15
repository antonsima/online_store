from unittest.mock import MagicMock

import pytest

from src.main import Category, LawnGrass, Product, Smartphone, BaseProduct


@pytest.fixture()
def mock_base_product():
    mock = MagicMock(spec=BaseProduct)
    mock.price.return_value = 'mocked price'
    mock.new_product.return_value = 'mocked new_product'
    mock.products.return_value = 'mocked products'

    return mock


@pytest.fixture()
def test_product_watermelon():
    return Product('Арбуз', 'Зеленый фрукт (или ягода)', 100, 10)


@pytest.fixture()
def test_product_orange():
    return Product('Апельсин', 'Лучший фрукт', 100, 10)


@pytest.fixture()
def test_product_apple():
    return Product('Яблоко', 'Кислый фрукт', 100, 10)


@pytest.fixture()
def test_product_qiwi():
    return Product('Киви', 'Тоже вкусно', 100, 5)


@pytest.fixture()
def test_smartphone():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0,
                      5, 95.5, "S23 Ultra", 256, "Серый")


@pytest.fixture()
def test_grass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20,
                     "Россия", "7 дней", "Зеленый")


@pytest.fixture()
def test_category_fruits(test_product_watermelon, test_product_orange, test_product_apple):
    return Category('Фрукты', 'Сладкая, вкусная еда', [test_product_watermelon,
                                                       test_product_orange,
                                                       test_product_apple])


@pytest.fixture()
def test_category_fruits_with_qiwi(test_product_watermelon, test_product_orange, test_product_apple,
                                   test_product_qiwi):
    return Category('Фрукты', 'Сладкая, вкусная еда', [test_product_watermelon,
                                                       test_product_orange,
                                                       test_product_apple,
                                                       test_product_qiwi])


@pytest.fixture()
def test_products_from_json():
    return [{'name': 'Смартфоны',
             'description': 'Смартфоны, как средство не только коммуникации, '
                            'но и получение дополнительных функций для удобства жизни',
             'products': [{'name': 'Samsung Galaxy C23 Ultra',
                           'description': '256GB, Серый цвет, 200MP камера',
                           'price': 180000.0,
                           'quantity': 5},
                          {'name': 'Iphone 15',
                           'description': '512GB, Gray space',
                           'price': 210000.0,
                           'quantity': 8},
                          {'name': 'Xiaomi Redmi Note 11',
                           'description': '1024GB, Синий',
                           'price': 31000.0,
                           'quantity': 14}]},
            {'name': 'Телевизоры',
             'description': 'Современный телевизор, который позволяет наслаждаться просмотром, '
                            'станет вашим другом и помощником',
             'products': [{'name': '55" QLED 4K',
                           'description': 'Фоновая подсветка',
                           'price': 123000.0,
                           'quantity': 7}]}]
