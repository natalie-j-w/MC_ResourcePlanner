from abc import ABC

class Resource(ABC):
    mod_id: str
    resource_id: str
    display_name: str
    max_stack: int
    recipes_where_output: ["Resource"]
    mineable: list["Resource"]  # example: only gets list from axe.json if item ID is in minecraft:axes
    img_path: str # TODO: Add images to resources

    def __init__(self, resource_id="", mod_id="", name="", max_stack=64):
        self.resource_id = resource_id
        self.display_name = name
        self.max_stack = max_stack
        self.mod_id = mod_id

    def __repr__(self):
        return repr(f"ID: {self.resource_id}, "
              f"Name: {self.display_name}, "
              f"Max Stack: {self.max_stack}, "
              f"Mod: {self.mod_id}")

    def _recipes_where_output(self) -> None:
        pass

    def _mineable(self) -> None:
        pass

    def add_image(self, img:str):
        self.img_path = img