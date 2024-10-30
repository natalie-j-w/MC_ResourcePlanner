from enum import Enum


class ResourceTypes(Enum):
    ITEM = "item"
    BLOCK = "block"
    TAG = "tag"
    FLUID = "fluid"
    UNKNOWN = "unknown"