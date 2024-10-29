from Planner import Resource, Recipe


class ResourceManager:
    def __init__(self):
        self.resources = {str: "Resource"}
        self.recipes = {"Resource": list["Recipe"]}

    def add_resource(self, resource:"Resource") -> None:
        # Resource ID is unique key, Resource is value
        r_id = resource.resource_id
        if not(r_id in self.resources.keys()):
            self.resources["r_id"] = resource

    def add_resource_from_json(self, json_dict:dict):
        # TODO: Resource from json
        pass

    def add_recipe(self, recipe:"Recipe") -> None:
        # get output resource IDs, use Resource with matching ID as key,list of recipes where Resource is in output list as value
        pass

    def get_resource_by_id(self, resource_id:str) -> "Resource":
        pass    # get resource with matching id from resources list

    def get_recipe_by_output_id(self) -> list["Recipe"]:
        pass    # return all recipes where resource with matching id is in output list


