from __future__ import annotations
import csv
from typing import TYPE_CHECKING,Union

if TYPE_CHECKING:
    from Planner import Resource, Recipe, Tag

from Resource import Resource
from Recipe import Recipe
from Tag import Tag

class DataManager:
    """
    Central manager for all resources, recipes and tags. Defines methods to load and retrieve data.
    """
    resources: {str: "Resource"}
    recipes: list["Recipe"]
    tags: {str: "Tag"}
    index_recipes_by_output: dict[Resource:list]

    def __init__(self):
        self.resources = {}
        self.recipes = []
        self.index_recipes_by_output = {}
        self.tags = {}

    def add_resource(self, resource:"Resource") -> None:
        """
        Adds given Resource to DataManager's list of all resources it not already in it
        :param resource: Resource to be added
        :return: None
        """
        r_id = resource.resource_id
        if not(r_id in self.resources.keys()):
            self.resources["r_id"] = resource
        else:
            print(f"{r_id} already in resource list")

    def add_resources_from_csv(self, csv_path:str) -> None:
        """
        :param csv_path: Full path to csv file with ItemName, ItemID, ModID and MaxStackSize column
        """

        with open(csv_path) as f:
            data = csv.DictReader(f)
            for row in data:
                new_resource = Resource(row["ItemID"],
                                        row["ModID"],
                                        row["ItemName"],
                                        row["MaxStackSize"])
                self.resources[new_resource.resource_id] = new_resource

    def add_recipe(self, recipe:"Recipe") -> None:
        """
        Adds given Recipe to DataManager's list of all recipes it not already in it
        :param recipe: Recipe to be added
        :return:
        """
        # get output resource IDs, use Resource with matching ID as key,list of recipes where Resource is in output list as value
        pass

    def add_tag(self, tag:"Tag"):
        """
        Adds given Tag to DataManager's list of all tags it not already in it
        Might update existing Tag if given Tag is already in list?
        :param tag: Tag to be added
        :return:
        """
        # TODO: Get tags for tags list
        # if tag not in list: add
        # if tag in list: retrieve by ID -> add resources to tag's list of resources
        pass

    def get_resource_or_tag_by_id(self, resource_id:str) -> Union[Resource, Tag]:
        """
        Retrieves a Tag or Resource by ID
        :param resource_id: ID of the resource or tag to be retrieved (example: "minecraft:anvil")
        :return: Resource if given ID is a resource; else Tag if given ID is a tag; else None
        """
        if self.resources.get(resource_id):
            return self.resources.get(resource_id)
        else:
            return self.tags.get(resource_id)

    def _recipes_output_index(self) -> None:
        # return all recipes where resource with matching id is in output list
        pass


