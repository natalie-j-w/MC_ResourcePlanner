from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Union
from dataclasses import dataclass
from FileManager import FileManager
from Units import Units

if TYPE_CHECKING:
    from Planner import (DataManager, Resource, Tag, JSONReader)


@dataclass
class RecipeItem:
    """
    Represents one resource in Recipe.inputs and Recipe.outputs.

    :param resource: (Tag | Resource, optional)
        A resource needed for the recipe.
    :param amount: (int, optional)
        Amount of resource needed for the recipe.
        Default: 0.
    :param amount_unit: (Units, optional)
        The unit represented by amount.
        Default: Units.REGULAR.
    :param multiple_alternatives: (list[Tag | Resource], optional)
        List of alternatives for ingredient slots where a variety of input resources is possible (for example in dye-ing recipes).
    """

    resource: Optional[Union[Resource, Tag]] = None
    amount: Optional[int] = None
    amount_unit: Optional[Units] = None
    multiple_alternatives: Optional[list[Union[Resource, Tag]]] = None

    def __init__(self, resource: Optional[Union[Resource, Tag]] = None,
                 amount: int = 0, amount_unit: Optional[Units] = None,
                 multiple_alternatives: Optional[list[Union[Resource, Tag]]] = None):
        self.resource = resource
        self.amount = amount
        self.amount_unit = amount_unit if amount_unit is not amount_unit is None else Units.REGULAR
        self.multiple_alternatives = multiple_alternatives


class Recipe:
    """
    Represents a recipe in the Minecraft crafting system, managing input and output resources, recipe type,
    processing time, and various specific recipe behaviors.

    Attributes:
    full_recipe_dict (dict):
        Full recipe data dictionary (typically loaded from a .json file).
        Contains complete recipe information including type, ingredients, result, etc.
    inputs (list[RecipeItem]):
        List of resources required for the recipe, created based on `full_recipe_dict`.
    outputs (list[RecipeItem]):
        List of resources produced by the recipe, created based on `full_recipe_dict`.
    recipe_type (str):
        Type of the recipe (e.g., 'minecraft:crafting_shaped', 'create:crushing'),
        which determines the process used for generating inputs and outputs.
    time_needed (int):
        Time required to complete the recipe. Default is 0.
    dm (DataManager):
        DataManager instance used to retrieve resource or tag information from the full dataset.

    Methods:
    __init__(recipe_dict: Optional[dict], resource_manager: Optional[DataManager],
             recipe_type: Optional[str], inputs: Optional[list[RecipeItem]],
             outputs: Optional[list[RecipeItem]], time_needed: int):
        Initializes a Recipe instance by either reading from a recipe dictionary (with DataManager), or
        by directly specifying recipe type, inputs, outputs, and processing time.

    print_all_crafting_types(recipes_path: str):
        Prints all unique recipe types found in JSON files within the specified directory.

    set_input_output(recipe_dict: dict):
        Sets the inputs and outputs for the recipe based on `recipe_type` and other data in `recipe_dict`.
        Calls specific processing functions based on the recipe type.

    Private Methods:
        __process_* (recipe_dict: dict): A series of private methods that handle various recipe types (e.g., shapeless, shaped, milling, smelting).
            These methods define the specific logic required to set inputs and outputs for each recipe type.
    """

    full_recipe_dict: dict
    inputs: list[RecipeItem]
    outputs: list[RecipeItem]
    recipe_type: str
    time_needed: int
    dm: DataManager

    def __init__(self, recipe_dict: Optional[dict] = None, resource_manager: Optional[DataManager] = None,
                 recipe_type: Optional[str] = None, inputs: Optional[list[RecipeItem]] = None,
                 outputs: Optional[list[RecipeItem]] = None, time_needed: int = 0):
        if recipe_dict is not None:
            self.full_recipe_dict = recipe_dict
            self.recipe_type = recipe_dict['type']
            self.inputs = []
            self.outputs = []
            self.time_needed = time_needed
            self.dm = resource_manager
            self.set_input_output(self.full_recipe_dict)

        elif recipe_type is not None and inputs is not None and outputs is not None:
            self.recipe_type = recipe_type
            self.inputs = inputs
            self.outputs = outputs
            self.time_needed = time_needed

        else:
            raise ValueError("Need either recipe_dict or recipe type, inputs and outputs")

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
        """
        Prints all crafting types found in .json recipes in recipes_path
        :param recipes_path:
        """
        import json

        all_types = set()

        try:
            for recipe in FileManager.find_json_files(recipes_path):
                print(recipe)
                with open(recipe) as f:
                    data = json.load(f)
                    all_types.add(data.get("type"))
        finally:
            for r in all_types:
                print(r)

    def set_input_output(self, recipe_dict:dict):
        """
        Sets the inputs and outputs for the recipe based on the recipe type and inputs + outputs provided in recipe_dict.

        :param recipe_dict: Dictionary containing recipe data. Ideally loaded with JSONReader.
                            This dictionary should include recipe type, input items, and output items.
        """

        new_inputs = []
        new_outputs = []
        new_processing_time = 0

        match self.recipe_type:
            # TODO: Define input output behavior for all recipe types
            # TODO: Define tag and liquid behavior (input can be tag, liquid or resource!)
            case "minecraft:crafting_shapeless":
                new_inputs, new_outputs, new_processing_time = self.__process_shapeless(recipe_dict)
            case "minecraft:crafting_shaped":
                new_inputs, new_outputs, new_processing_time = self.__process_shaped(recipe_dict)
            case "minecraft:stonecutting":
                new_inputs, new_outputs, new_processing_time = self.__process_stonecutting(recipe_dict)
            case "minecraft:smelting":
                new_inputs, new_outputs, new_processing_time = self.__process_smelting(recipe_dict)
            case "minecraft:blasting":
                new_inputs, new_outputs, new_processing_time = self.__process_blasting(recipe_dict)
            case "minecraft:campfire_cooking":
                new_inputs, new_outputs, new_processing_time = self.__process_campfire_cooking(recipe_dict)
            case "minecraft:smoking":
                new_inputs, new_outputs, new_processing_time = self.__process_smoking(recipe_dict)
            case "minecraft:smithing_transform":
                new_inputs, new_outputs, new_processing_time = self.__process_smithing_transform(recipe_dict)
            case "minecraft:smithing_trim":
                new_inputs, new_outputs, new_processing_time = self.__process_smithing_trim(recipe_dict)
            case "create:milling":
                new_inputs, new_outputs, new_processing_time = self.__process_milling(recipe_dict)
            case "create:pressing":
                new_inputs, new_outputs, new_processing_time = self.__process_pressing(recipe_dict)
            case "create:splashing":
                new_inputs, new_outputs, new_processing_time = self.__process_splashing(recipe_dict)
            case "create:emptying":
                new_inputs, new_outputs, new_processing_time = self.__process_emptying(recipe_dict)
            case "create:filling":
                new_inputs, new_outputs, new_processing_time = self.__process_filling(recipe_dict)
            case "create:crushing":
                new_inputs, new_outputs, new_processing_time = self.__process_crushing(recipe_dict)
            case "create:mechanical_crafting":
                new_inputs, new_outputs, new_processing_time = self.__process_mechanical_crafting(recipe_dict)
            case "create:sandpaper_polishing":
                new_inputs, new_outputs, new_processing_time = self.__process_sandpaper_polishing(recipe_dict)
            case "create:item_application":
                new_inputs, new_outputs, new_processing_time = self.__process_item_application(recipe_dict)
            case "create:mixing":
                new_inputs, new_outputs, new_processing_time = self.__process_mixing(recipe_dict)
            case "create:sequenced_assembly":
                new_inputs, new_outputs, new_processing_time = self.__process_sequenced_assembly(recipe_dict)
            case "create:cutting":
                new_inputs, new_outputs, new_processing_time = self.__process_cutting(recipe_dict)
            case "create:deploying":
                new_inputs, new_outputs, new_processing_time = self.__process_deploying(recipe_dict)
            case "create:compacting":
                new_inputs, new_outputs, new_processing_time = self.__process_compacting(recipe_dict)
            case "create:haunting":
                new_inputs, new_outputs, new_processing_time = self.__process_haunting(recipe_dict)
            case _:
                pass

        self.inputs = new_inputs
        self.outputs = new_outputs
        self.time_needed = new_processing_time

    def __process_shapeless(self, recipe_dict:dict) -> (list[RecipeItem], list[RecipeItem], int):
        new_in = []
        new_out = []

        # Determine input resources and counts
        inputs_dict = {}
        for item in recipe_dict.get("ingredients"):
            key = item.get("item") or item.get("tag")
            inputs_dict[key] = inputs_dict.get(key, 0) + 1

        for input_item in inputs_dict:
            resource = self.dm.get_resource_or_tag_by_id(input_item)
            count = inputs_dict[input_item]
            new_in.append(RecipeItem(resource, count))

        # Determine output
        result = recipe_dict.get("result")
        result_resource = self.dm.get_resource_or_tag_by_id(result.get("item"))
        new_out.append(RecipeItem(result_resource, result.get("count", 1)))

        return new_in, new_out, 0

    def __process_shaped(self, recipe_dict:dict) -> (list[RecipeItem], list[RecipeItem], int):
        new_in = []
        new_out = []

        keys = recipe_dict.get("key")
        pattern = "".join(recipe_dict.get("pattern", ""))

        try:
            if keys is not None:
                for key in keys:
                    input_amount = pattern.count(key)
                    if keys[key].get("item"):
                        input_item = keys[key].get("item")
                    elif keys[key].get("tag"):
                        # TODO: Get Tag from DataManager for Recipe input
                        input_item = keys[key].get("tag")
                    else:
                        input_item = ""

                    input_resource = self.dm.get_resource_or_tag_by_id(input_item)
                    new_in.append(RecipeItem(input_resource, input_amount))

            result = self.dm.get_resource_or_tag_by_id(recipe_dict["result"]["item"])
            result_amount = recipe_dict.get("result", {}).get("count", 1)
            new_out.append(RecipeItem(result, result_amount))

        except Exception as e:
            print(f"Error: {e}")

        return new_in, new_out, 0

    def __process_stonecutting(self, recipe_dict:dict) -> (list[RecipeItem], list[RecipeItem], int):
        pass

    def __process_smelting(self, recipe_dict:dict) -> (list[RecipeItem], list[RecipeItem], int):
        pass

    def __process_blasting(self, recipe_dict:dict) -> (list[RecipeItem], list[RecipeItem], int):
        pass

    def __process_campfire_cooking(self, recipe_dict:dict) -> (list[RecipeItem], list[RecipeItem], int):
        pass

    def __process_smoking(self, recipe_dict:dict) -> (list[RecipeItem], list[RecipeItem], int):
        pass

    def __process_smithing_transform(self, recipe_dict:dict) -> (list[RecipeItem], list[RecipeItem], int):
        pass

    def __process_smithing_trim(self, recipe_dict:dict) -> (list[RecipeItem], list[RecipeItem], int):
        pass

    def __process_milling(self, recipe_dict:dict) -> (list[RecipeItem], list[RecipeItem], int):
        pass

    def __process_pressing(self, recipe_dict:dict) -> (list[RecipeItem], list[RecipeItem], int):
        pass

    def __process_splashing(self, recipe_dict:dict) -> (list[RecipeItem], list[RecipeItem], int):
        pass

    def __process_emptying(self, recipe_dict:dict) -> (list[RecipeItem], list[RecipeItem], int):
        pass

    def __process_filling(self, recipe_dict:dict) -> (list[RecipeItem], list[RecipeItem], int):
        pass

    def __process_crushing(self, recipe_dict:dict) -> (list[RecipeItem], list[RecipeItem], int):
        pass

    def __process_mechanical_crafting(self, recipe_dict:dict) -> (list[RecipeItem], list[RecipeItem], int):
        pass

    def __process_sandpaper_polishing(self, recipe_dict:dict) -> (list[RecipeItem], list[RecipeItem], int):
        pass

    def __process_item_application(self, recipe_dict:dict) -> (list[RecipeItem], list[RecipeItem], int):
        pass

    def __process_mixing(self, recipe_dict:dict) -> (list[RecipeItem], list[RecipeItem], int):
        pass

    def __process_sequenced_assembly(self, recipe_dict:dict) -> (list[RecipeItem], list[RecipeItem], int):
        pass

    def __process_cutting(self, recipe_dict:dict) -> (list[RecipeItem], list[RecipeItem], int):
        pass

    def __process_deploying(self, recipe_dict:dict) -> (list[RecipeItem], list[RecipeItem], int):
        pass

    def __process_compacting(self, recipe_dict:dict) -> (list[RecipeItem], list[RecipeItem], int):
        pass

    def __process_haunting(self, recipe_dict:dict) -> (list[RecipeItem], list[RecipeItem], int):
        pass