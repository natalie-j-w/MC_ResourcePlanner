from re import match
from typing import TypedDict

class Recipe:
    class _RecipeInputOutput(TypedDict):
        resource: "Resource"
        count: int

    input: list[_RecipeInputOutput]
    output: list[_RecipeInputOutput]
    recipe_type: str

    def __init__(self, recipe_dict):
        self.recipe_type = recipe_dict['type']
        self.get_input_output()

    def get_input_output(self):
        from Planner import Resource

        match self.recipe_type:
            case "":
                empty_resource = Resource("", "", 0)
                self.input = [Recipe._RecipeInputOutput(resource=empty_resource, count=0)]
                self.input = [Recipe._RecipeInputOutput(resource=empty_resource, count=0)]
            case "minecraft:crafting_shapeless":
                pass
            case "minecraft:crafting_shaped":
                pass
            case _:
                pass