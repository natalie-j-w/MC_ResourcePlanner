from abc import ABC, abstractmethod
from Recipe import Recipe
import ResourceTypes


class Resource(ABC):
    resource_type: ResourceTypes
    resource_id: str
    display_name: str
    max_stack: int

    def __init__(self, resource_type: ResourceTypes, resource_id: str, name: str, max_stack: int):
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.display_name = name
        self.max_stack = max_stack

    @abstractmethod
    def print_info(self) -> None:
        pass

    @abstractmethod
    def get_recipes(self) -> list[Recipe]:
        pass