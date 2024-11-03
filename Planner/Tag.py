from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Planner import Resource

class Tag:
    mod_id: str
    tag_id: str
    resources: list[Resource]

    def __init__(self, mod_id, tag_id):
        self.mod_id = mod_id
        self.tag_id = tag_id

    def __repr__(self):
        return f"Tag(Mod:\"{self.mod_id}\", Tag ID:\"{self.tag_id}\")"