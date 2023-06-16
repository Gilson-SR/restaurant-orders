from src.models.ingredient import (
    Ingredient,
    Restriction,
    )  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    first_ingredient = Ingredient("Shiitake")
    second_ingredient = Ingredient("Shiitake")
    third_ingredient = Ingredient("Shimeji")

    assert first_ingredient.name == "Shiitake"
    assert first_ingredient.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

    assert first_ingredient.__repr__() == "Ingredient('Shiitake')"

    assert first_ingredient == second_ingredient
    assert first_ingredient != third_ingredient
    assert hash(first_ingredient) == hash(second_ingredient)
    assert hash(first_ingredient) != hash(third_ingredient)
