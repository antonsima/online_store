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
