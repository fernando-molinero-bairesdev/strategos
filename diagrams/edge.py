from __future__ import annotations
from typing import Dict, Any
import uuid
from drawing import registry

class Edge:
    def __init__(self,
                 diagram: "Diagram",
                 name: str,
                 source_id: str,
                 target_id: str,
                 description: str = "",
                 id: str | None = None,
                 template_name: str = "line"):
        self.diagram = diagram
        self.id = id if id is not None else str(uuid.uuid4())
        self.name = name
        self.source_id = source_id
        self.target_id = target_id
        self.description = description
        self.template_name = template_name

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "source_id": self.source_id,
            "target_id": self.target_id,
            "description": self.description,
            "template_name": self.template_name,
        }

    def draw(self) -> str:
        template = registry.get(self.template_name)
        if not template:
            template = registry.get("line")  # Fallback
        source = self.diagram.nodes.get(self.source_id)
        target = self.diagram.nodes.get(self.target_id)
        return template.draw(**{'x1': source.x, 'y1': source.y, 'x2': target.x, 'y2': target.y})

    @classmethod
    def from_dict(cls, diagram: "Diagram", data: Dict) -> Edge:
        return cls(
            id=data.get("id") or str(uuid.uuid4()),
            name=data["name"],
            diagram=diagram,
            source_id=data["source_id"],
            target_id=data["target_id"],
            description=data.get("description", ""),
            template_name=data.get("template_name", "line"),
        )
