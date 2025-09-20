from typing import Dict, List, Tuple
import uuid
from .node import Node
from .edge import Edge

class Diagram:
    def __init__(self, id: str | None = None):
        self.id = id if id is not None else str(uuid.uuid4())
        self.name: str = ""
        self.description: str = ""
        self.filename: str = ""
        self.nodes: Dict[str, Node] = {}
        self.edges: Dict[str, Edge] = {}

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "filename": self.filename,
            "nodes": {name: node.to_dict() for name, node in self.nodes.items()},
            "edges": {name: edge.to_dict() for name, edge in self.edges.items()},
            "diagram": self.draw(),
        }

    def add_node(self, node: Node) -> None:
        self.nodes[node.name] = node

    def add_edge(self, edge: Edge) -> None:
        self.edges[edge.name] = edge

    def list_nodes(self) -> List[Node]:
        return [n for n in self.nodes.values()]

    def list_edges(self) -> List[Edge]:
        return [e for e in self.edges.values()]

    def set_default_positions(self) -> None:
        # Simple grid layout for demonstration
        cols = int(len(self.nodes) ** 0.5) + 1
        for idx, node in enumerate(self.list_nodes()):
            node.x = (idx % cols) * 100 + 50
            node.y = (idx // cols) * 100 + 50

    def draw(self) -> None:
        # Placeholder for drawing logic
        self.set_default_positions()
        results = []
        for node in self.list_nodes():
            results.append(node.draw())
        for edge in self.list_edges():
            results.append(edge.draw())
        print("\n".join(results))
        return results

    @classmethod
    def from_dict(cls, data: Dict) -> "Diagram":
        diagram = cls(id=data.get("id"))
        diagram.name = data.get("name", "")
        diagram.description = data.get("description", "")
        diagram.filename = data.get("filename", "")
        for name, node_data in data.get("nodes", {}).items():
            diagram.nodes[name] = Node.from_dict(diagram, node_data)
        for name, edge_data in data.get("edges", {}).items():
            diagram.edges[name] = Edge.from_dict(diagram, edge_data)
        return diagram
