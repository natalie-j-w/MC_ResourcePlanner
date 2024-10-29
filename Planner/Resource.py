from abc import ABC

class Resource(ABC):
    mod_id: str
    resource_id: str
    display_name: str
    max_stack: int
    recipes_where_output: ["Resource"]
    mineable: list["Resource"]

    def __init__(self, resource_id: str, name: str, max_stack: int, mod_id:str):
        self.resource_id = resource_id
        self.display_name = name
        self.max_stack = max_stack
        self.mod_id = mod_id

    def create_from_json(self, json_dict:dict):
        pass

    def print_info(self) -> None:
        pass

    def _recipes_where_output(self) -> None:
        pass

    def _mineable(self) -> None:
        pass

    def __repr__(self):
        return repr(f"ID: {self.resource_id}, "
              f"Name: {self.display_name}, "
              f"Max Stack: {self.max_stack}, "
              f"Mod: {self.mod_id}")