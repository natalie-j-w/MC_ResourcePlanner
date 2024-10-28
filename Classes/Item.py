import Resource
from ResourceTypes import ResourceTypes
from ToolTypes import ToolTypes


class Item(Resource):
    isTool = False
    toolType = None

    def __init__(self, resource_id: str, name: str, max_stack: int, toolType: ToolTypes, resource_type=ResourceTypes.ITEM):
        super().__init__(self, resource_id, name, max_stack, resource_type)
        self.toolType = toolType
        self.isTool = True if (self.toolType is not None) else False

