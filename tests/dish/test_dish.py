from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import (
    Ingredient,
)
import pytest


# Req 2
def test_dish():
    dish = Dish("Pizza", 15.99)
    assert dish.name == "Pizza"
    assert dish.__repr__() == "Dish('Pizza', R$15.99)"

    dish2 = Dish("Pizza", 15.99)
    assert dish == dish2
    assert dish.__hash__() == dish2.__hash__()

    dish3 = Dish("Sushi", 12.99)
    assert dish != dish3
    assert dish.__hash__() != dish3.__hash__()

    with pytest.raises(TypeError):
        Dish("name", "price")
    with pytest.raises(ValueError):
        Dish("name", 0)

    dish.add_ingredient_dependency(Ingredient("Tomate"), 3)
    assert dish.recipe.get(Ingredient("Tomate")) == 3
    assert dish.get_restrictions() == set()

    dish.add_ingredient_dependency(Ingredient("Queijo"), 2)
    assert dish.get_ingredients() == {
        Ingredient("Tomate"),
        Ingredient("Queijo")
    }
    assert dish.get_restrictions() == set()
