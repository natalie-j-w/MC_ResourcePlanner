import Resource
from ToolTypes import ToolTypes


class Item(Resource):
    isTool = False
    toolType = None

    def __init__(self, resource_id: str, name: str, max_stack: int, toolType: ToolTypes):
        super().__init__(self, resource_id, name, max_stack)
        self.toolType = toolType
        self.isTool = True if (self.toolType is not None) else False

