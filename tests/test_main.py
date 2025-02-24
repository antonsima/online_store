from src.main import Category


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

    assert Category.category_quantity == 2
    assert Category.products_quantity == 7
