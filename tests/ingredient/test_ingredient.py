from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    first_ingredient = Ingredient("queijo gorgonzola")
    second_ingredient = Ingredient("queijo gorgonzola")
    third_ingredient = Ingredient("queijo provolone")
    assert first_ingredient.name == "queijo gorgonzola"
    assert first_ingredient.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

    assert repr(first_ingredient) == "Ingredient('queijo gorgonzola')"

    assert first_ingredient != third_ingredient
    assert first_ingredient == second_ingredient
    assert hash(first_ingredient) != hash(third_ingredient)
    assert hash(first_ingredient) == hash(second_ingredient)
