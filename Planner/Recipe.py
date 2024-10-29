from re import match
from typing import TypedDict

class Recipe:
    class _RecipeInputOutput(TypedDict):
        resource: "Resource"
        count: int

    input: list[_RecipeInputOutput]
    output: list[_RecipeInputOutput]
    recipe_type: str
    rm: "ResourceManager"

    def __init__(self, recipe_dict:dict, resource_manager: "ResourceManager"):
        self.recipe_type = recipe_dict['type']
        self.input = []
        self.output = []
        self.rm = resource_manager

        self.get_input_output(recipe_dict)


    def __repr__(self):
        return repr(f"Inputs: {self.input}, "
                    f"Outputs: {self.output}, "
                    f"Type: {self.recipe_type}")

    def get_input_output(self, recipe_dict):
        from Planner import Resource

        match self.recipe_type:
            # TODO: Define input output behavior for all recipe types
            case "":
                empty_resource = Resource("", "", 0, "")
                self.input = [Recipe._RecipeInputOutput(resource=empty_resource, count=0)]
                self.output = [Recipe._RecipeInputOutput(resource=empty_resource, count=0)]
            case "minecraft:crafting_shapeless":
                pass
            case "minecraft:crafting_shaped":
                keys = recipe_dict.get("key")
                pattern = "".join(recipe_dict.get("pattern"))

                try:
                    if keys is not None:
                        for key in keys:
                            input_amount = pattern.count(key)
                            if keys[key].get("item"):
                                input_resource = keys[key].get("item")
                            elif keys[key].get("tag"):
                                # TODO: Define better tag behavior
                                input_resource = keys[key].get("tag")
                            else:
                                input_resource = None
                            self.input.append(Recipe._RecipeInputOutput(resource=input_resource, count=input_amount))

                    out_item = self.rm.get_resource_by_id(recipe_dict["result"]["item"])
                    self.output = [Recipe._RecipeInputOutput(resource=out_item, count=1)]
                except Exception as e:
                    print(f"{e} AAAAAAAAAAA")
            case _:
                pass