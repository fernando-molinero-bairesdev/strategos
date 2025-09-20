from __future__ import annotations
from typing import Dict, Any, Optional
import uuid
from drawing import registry

class Node:
    def __init__(self,
                 diagram: "Diagram",
                 name: str,
                 description: str = "",
                 id: str | None = None,
                 x: Optional[int] = None,
                 y: Optional[int] = None,
                 size: Optional[int] = 10,
                 template_name: str = "circle",
                 dependent: bool = False):
        self.x = x
        self.y = y
        self.size = size
        self.diagram = diagram
        self.id = id if id is not None else str(uuid.uuid4())
        self.name = name
        self.description = description
        self.template_name = template_name
        self.dependent = dependent

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "template_name": self.template_name,
            "dependent": self.dependent,
            "x": self.x,
            "y": self.y,
        }

    def draw(self) -> str:
        template = registry.get(self.template_name)
        if not template:
            template = registry.get("circle")  # Fallback
        return template.draw(label=self.name, **self.to_dict())

    @classmethod
    def from_dict(cls, diagram: "Diagram", data: Dict) -> Node:
        return cls(
            diagram=diagram.id,
            id=data.get("id"),
            name=data["name"],
            description=data.get("description", ""),
            template_name=data.get("template_name", "circle"),
            dependent=data.get("dependent", False),
        )
