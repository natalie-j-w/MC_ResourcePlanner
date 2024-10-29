from abc import ABC, abstractmethod

class Resource(ABC):
    resource_id: str
    display_name: str
    max_stack: int
    recipes_where_output: ["Resource"]
    mineable: list["Resource"]

    def __init__(self, resource_id: str, name: str, max_stack: int):
        self.resource_id = resource_id
        self.display_name = name
        self.max_stack = max_stack

    def create_from_json(self, json_dict:dict):
        pass

    def print_info(self) -> None:
        pass

    def _recipes_where_output(self) -> None:
        pass

    def _mineable(self) -> None:
        pass