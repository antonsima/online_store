import pytest

from src.main import Category, Product


@pytest.fixture()
def test_product_watermelon():
    return Product('Арбуз', 'Зеленый фрукт (или ягода)', 100, 10)


@pytest.fixture()
def test_category_fruits():
    return Category('Фрукты', 'Сладкая, вкусная еда', ['Банан', 'Яблоко', 'Апельсин'])


@pytest.fixture()
def test_category_vegetables():
    return Category('Овощи', 'Полезная еда', ['Картошка', 'Помидор', 'Огурец', 'Свекла'])


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
