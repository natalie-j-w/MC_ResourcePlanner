from typing import TypedDict
from Resource import Resource

class Recipe:
    class _RecipeInputOutput(TypedDict):
        resource: Resource
        count: int

    input: list[_RecipeInputOutput]
    output: list[_RecipeInputOutput]
    recipe_type: str

    def __init__(self, input_resources: list[_RecipeInputOutput], output_resources: list[_RecipeInputOutput], ):
        self.input = input_resources
        self.output = output_resources

    def get_input(self):
        pass

    def get_output(self):
        pass
