from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Union
from dataclasses import dataclass
from Units import Units

if TYPE_CHECKING:
    from Planner import (DataManager, Resource, Tag)
    from Units import Units

@dataclass
class RecipeItem:
    resource: Optional[Union[Resource, Tag]] = None
    amount: Optional[int] = None
    amount_unit: Optional[Units] = None

    def __init__(self, resource: Optional[Union[Resource, Tag]] = None, amount: int = 0, amount_unit: Optional[Units] = None):
        self.resource = resource or None
        self.amount = amount
        self.amount_unit = amount_unit if amount_unit is not None else Units.REGULAR

class Recipe:
    inputs: list[RecipeItem]
    outputs: list[RecipeItem]
    recipe_type: str
    rm: DataManager

    def __init__(self, recipe_dict:dict, resource_manager: DataManager):
        self.recipe_type = recipe_dict['type']
        self.inputs = []
        self.outputs = []
        self.rm = resource_manager

        self.get_input_output(recipe_dict)

    def __repr__(self):
        return repr(f"Inputs: {self.inputs}, "
                    f"Outputs: {self.outputs}, "
                    f"Type: {self.recipe_type}")

    def __eq__(self, other:Recipe):
        return all([self.recipe_type == other.recipe_type,
                    self.inputs == other.inputs,
                    self.outputs == other.outputs])

    def get_input_output(self, recipe_dict:dict):
        match self.recipe_type:
            # TODO: Define input output behavior for all recipe types
            # TODO: Define tag and liquid behavior (input can be tag, liquid or resource!)
            case "minecraft:crafting_shapeless":
                self.__process_shapeless(recipe_dict)
            case "minecraft:crafting_shaped":
                self.__process_shaped(recipe_dict)
            case _:
                pass

    def __process_shapeless(self, recipe_dict:dict):
        pass

    def __process_shaped(self, recipe_dict:dict):
        keys = recipe_dict.get("key")
        pattern = "".join(recipe_dict.get("pattern", ""))

        try:
            if keys is not None:
                for key in keys:
                    input_amount = pattern.count(key)
                    if keys[key].get("item"):
                        input_resource = keys[key].get("item")
                    elif keys[key].get("tag"):
                        input_resource = keys[key].get("tag")
                    else:
                        input_resource = None
                    self.inputs.append(RecipeItem(input_resource, input_amount))

            out_resource = self.rm.get_resource_or_tag_by_id(recipe_dict["result"]["item"])
            out_count = recipe_dict.get("result", {}).get("count", 1)
            self.outputs.append(RecipeItem(out_resource, out_count))

        except Exception as e:
            print(f"Error: {e}")