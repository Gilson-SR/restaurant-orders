from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import (
    Ingredient,
    Restriction,
)
import pytest


# Req 2
def test_dish():
    dish = Dish("pizza", 50.0)
    dish2 = Dish("shimeji", 14.0)
    dish3 = Dish("pizza", 50.0)

    assert dish.name == 'pizza'
    assert dish.price == 50.0

    assert dish != dish2
    assert dish == dish3

    assert hash(dish) != hash(dish2)
    assert hash(dish) == hash(dish3)

    ingredient = Ingredient("queijo gorgonzola")
    dish.add_ingredient_dependency(ingredient, 200)
    assert ingredient in dish.get_ingredients()

    assert dish.get_restrictions() == set()

    assert str(dish) == "Dish('pizza', R$50.00)"

    with pytest.raises(ValueError):
        Dish("pizza", -50)
