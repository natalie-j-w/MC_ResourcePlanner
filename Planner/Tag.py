from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Planner import Resource

class Tag:
    mod_id: str
    name: str
    resources: list[Resource]

    def __init__(self, mod_id, name):
        self.mod_id = mod_id
        self.name = name