from unittest.mock import patch

from src.main import get_categories_and_products_from_json_file, Category


def test_product(test_product_watermelon):
    watermelon = test_product_watermelon
    assert watermelon.name == 'Арбуз'
    assert watermelon.description == 'Зеленый фрукт (или ягода)'
    assert watermelon.price == 100
    assert watermelon.quantity == 10


def test_category(test_category_fruits, test_category_vegetables):
    fruits = test_category_fruits
    assert fruits.name == 'Фрукты'
    assert fruits.description == 'Сладкая, вкусная еда'
    assert fruits.products == ['Банан', 'Яблоко', 'Апельсин']

    vegetables = test_category_vegetables
    assert vegetables.name == 'Овощи'
    assert vegetables.description == 'Полезная еда'
    assert vegetables.products == ['Картошка', 'Помидор', 'Огурец', 'Свекла']


@patch('json.load')
def test_get_categories_and_products_from_json_file(mock_load, test_products_from_json):
    mock_load.return_value = test_products_from_json
    categories_obj, products_obj = get_categories_and_products_from_json_file('products.json')

    assert categories_obj['Смартфоны'].name == 'Смартфоны'
    assert (categories_obj['Смартфоны'].description == 'Смартфоны, как средство не только коммуникации, '
                                                       'но и получение дополнительных функций для удобства жизни')
    assert categories_obj['Телевизоры'].name == 'Телевизоры'
    assert (categories_obj['Телевизоры'].description == 'Современный телевизор, который позволяет '
                                                        'наслаждаться просмотром, станет вашим другом и помощником')

    assert products_obj['Samsung Galaxy C23 Ultra'].name == 'Samsung Galaxy C23 Ultra'
    assert products_obj['Samsung Galaxy C23 Ultra'].description == '256GB, Серый цвет, 200MP камера'
    assert products_obj['Samsung Galaxy C23 Ultra'].price == 180000
    assert products_obj['Samsung Galaxy C23 Ultra'].quantity == 5

    assert products_obj['Iphone 15'].name == 'Iphone 15'
    assert products_obj['Iphone 15'].description == '512GB, Gray space'
    assert products_obj['Iphone 15'].price == 210000
    assert products_obj['Iphone 15'].quantity == 8

    assert products_obj['Xiaomi Redmi Note 11'].name == 'Xiaomi Redmi Note 11'
    assert products_obj['Xiaomi Redmi Note 11'].description == '1024GB, Синий'
    assert products_obj['Xiaomi Redmi Note 11'].price == 31000
    assert products_obj['Xiaomi Redmi Note 11'].quantity == 14

    assert products_obj['55" QLED 4K'].name == '55" QLED 4K'
    assert products_obj['55" QLED 4K'].description == 'Фоновая подсветка'
    assert products_obj['55" QLED 4K'].price == 123000
    assert products_obj['55" QLED 4K'].quantity == 7

    assert Category.category_count == 4
    assert Category.product_count == 11
