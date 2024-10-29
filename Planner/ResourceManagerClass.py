import csv
from Planner import Resource, Recipe


class ResourceManager:
    def __init__(self):
        self.resources = {str: "Resource"}
        self.recipes = list["Recipe"]
        self.recipe_output_index = dict[Resource:list[Recipe]]
        # TODO: Get tags for tags list
        self.tags = list["Tag"]

    def add_resource(self, resource:"Resource") -> None:
        # Resource ID is unique key, Resource is value
        r_id = resource.resource_id
        if not(r_id in self.resources.keys()):
            self.resources["r_id"] = resource
        else:
            print(f"{r_id} already in resource list")

    def add_resources_from_csv(self, csv_path:str) -> None:
        """
        :param csv_path: Expects csv with ItemName, ItemID and MaxStackSize column
        """

        with open(csv_path) as f:
            data = csv.DictReader(f)
            for row in data:
                new_resource = Resource(row["ItemID"],
                                        row["ItemName"],
                                        row["MaxStackSize"],
                                        row["ModID"])
                self.resources[new_resource.resource_id] = new_resource

    def add_recipe(self, recipe:"Recipe") -> None:
        # get output resource IDs, use Resource with matching ID as key,list of recipes where Resource is in output list as value
        pass

    def get_resource_by_id(self, resource_id:str) -> "Resource":
        return self.resources.get(resource_id)

    def _recipes_output_index(self, output_resource:"Resource") -> None:
        # return all recipes where resource with matching id is in output list
        pass


