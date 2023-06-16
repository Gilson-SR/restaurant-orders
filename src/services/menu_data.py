from src.models.dish import Dish
from src.models.ingredient import Ingredient
import pandas as pd


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        data = pd.read_csv(source_path)

        for ingredients in data["dish"].unique():
            diference = data[data["dish"] == ingredients]
            price = diference["price"].iloc[0]
            new = Dish(ingredients, price)
            ingredient = diference[["ingredient", "recipe_amount"]].values.tolist()
            for i1, i2 in ingredient:
                ingrendient_result = Ingredient(i1)
                new.add_ingredient_dependency(ingrendient_result, i2)
            self.dishes.add(new)
