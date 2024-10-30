from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Union
from dataclasses import dataclass
from FileManager import FileManager

if TYPE_CHECKING:
    from Planner import (DataManager, Resource, Tag, JSONReader)
    from Units import Units

@dataclass
class RecipeItem:
    """
    Represents one resource in Recipe.inputs and Recipe.outputs
    """
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

    @staticmethod
    def print_all_crafting_types(recipes_path):
        import json

        all_types = set()

        for recipe in FileManager.find_json_files(recipes_path):
            print(recipe)
            with open(recipe) as f:
                data = json.load(f)
                all_types.add(data.get("type"))

        for r in all_types:
            print(r)

    def get_input_output(self, recipe_dict:dict):
        match self.recipe_type:
            # TODO: Define input output behavior for all recipe types
            # TODO: Define tag and liquid behavior (input can be tag, liquid or resource!)
            case "minecraft:crafting_shapeless":
                self.__process_shapeless(recipe_dict)
            case "minecraft:crafting_shaped":
                self.__process_shaped(recipe_dict)
            case "minecraft:stonecutting":
                self.__process_stonecutting(recipe_dict)
            case "minecraft:smelting":
                self.__process_smelting(recipe_dict)
            case "minecraft:blasting":
                self.__process_blasting(recipe_dict)
            case "minecraft:campfire_cooking":
                self.__process_campfire_cooking(recipe_dict)
            case "minecraft:smoking":
                self.__process_smoking(recipe_dict)
            case "minecraft:smithing_transform":
                self.__process_smithing_transform(recipe_dict)
            case "minecraft:smithing_trim":
                self.__process_smithing_trim(recipe_dict)
            case "create:milling":
                self.__process_milling(recipe_dict)
            case "create:pressing":
                self.__process_pressing(recipe_dict)
            case "create:splashing":
                self.__process_splashing(recipe_dict)
            case "create:emptying":
                self.__process_emptying(recipe_dict)
            case "create:filling":
                self.__process_filling(recipe_dict)
            case "create:crushing":
                self.__process_crushing(recipe_dict)
            case "create:mechanical_crafting":
                self.__process_mechanical_crafting(recipe_dict)
            case "create:sandpaper_polishing":
                self.__process_sandpaper_polishing(recipe_dict)
            case "create:item_application":
                self.__process_item_application(recipe_dict)
            case "create:mixing":
                self.__process_mixing(recipe_dict)
            case "create:sequenced_assembly":
                self.__process_sequenced_assembly(recipe_dict)
            case "create:cutting":
                self.__process_cutting(recipe_dict)
            case "create:deploying":
                self.__process_deploying(recipe_dict)
            case "create:compacting":
                self.__process_compacting(recipe_dict)
            case "create:haunting":
                self.__process_haunting(recipe_dict)
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

    def __process_stonecutting(self, recipe_dict:dict):
        pass

    def __process_smelting(self, recipe_dict:dict):
        pass

    def __process_blasting(self, recipe_dict:dict):
        pass

    def __process_campfire_cooking(self, recipe_dict:dict):
        pass

    def __process_smoking(self, recipe_dict:dict):
        pass

    def __process_smithing_transform(self, recipe_dict:dict):
        pass

    def __process_smithing_trim(self, recipe_dict: dict):
        pass

    def __process_milling(self, recipe_dict:dict):
        pass

    def __process_pressing(self, recipe_dict:dict):
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

    def __process_splashing(self, recipe_dict:dict):
        pass

    def __process_emptying(self, recipe_dict:dict):
        pass

    def __process_filling(self, recipe_dict:dict):
        pass

    def __process_crushing(self, recipe_dict:dict):
        pass

    def __process_mechanical_crafting(self, recipe_dict:dict):
        pass

    def __process_sandpaper_polishing(self, recipe_dict:dict):
        pass

    def __process_item_application(self, recipe_dict: dict):
        pass

    def __process_mixing(self, recipe_dict:dict):
        pass

    def __process_sequenced_assembly(self, recipe_dict:dict):
        pass

    def __process_cutting(self, recipe_dict:dict):
        pass

    def __process_deploying(self, recipe_dict: dict):
        pass

    def __process_compacting(self, recipe_dict:dict):
        pass

    def __process_haunting(self, recipe_dict: dict):
        pass