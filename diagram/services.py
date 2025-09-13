"""
Diagram services for the diagram package.
"""

from typing import List, Dict, Any
from datetime import datetime
from .models import DiagramModel, DiagramResponse, NodeModel, EdgeModel, DiagramType


class DiagramService:
    """Service class for diagram operations."""
    
    def __init__(self):
        """Initialize the diagram service with in-memory storage."""
        self._diagram_store: Dict[int, DiagramResponse] = {}
        self._next_id = 1
    
    def get_all_diagrams(self) -> List[DiagramResponse]:
        """Get all diagrams."""
        return list(self._diagram_store.values())
    
    def create_diagram(self, diagram: DiagramModel) -> DiagramResponse:
        """Create a new diagram."""
        now = datetime.utcnow()
        diagram_response = DiagramResponse(
            id=self._next_id,
            title=diagram.title,
            diagram_type=diagram.diagram_type,
            description=diagram.description,
            nodes=diagram.nodes,
            edges=diagram.edges,
            metadata=diagram.metadata,
            created_at=now,
            updated_at=now,
            node_count=len(diagram.nodes),
            edge_count=len(diagram.edges)
        )
        self._diagram_store[self._next_id] = diagram_response
        self._next_id += 1
        return diagram_response
    
    def get_diagram(self, diagram_id: int) -> DiagramResponse:
        """Get a specific diagram by ID."""
        if diagram_id not in self._diagram_store:
            raise ValueError(f"Diagram with ID {diagram_id} not found")
        return self._diagram_store[diagram_id]
    
    def update_diagram(self, diagram_id: int, diagram: DiagramModel) -> DiagramResponse:
        """Update a specific diagram."""
        if diagram_id not in self._diagram_store:
            raise ValueError(f"Diagram with ID {diagram_id} not found")
        
        existing_diagram = self._diagram_store[diagram_id]
        updated_diagram = DiagramResponse(
            id=existing_diagram.id,
            title=diagram.title,
            diagram_type=diagram.diagram_type,
            description=diagram.description,
            nodes=diagram.nodes,
            edges=diagram.edges,
            metadata=diagram.metadata,
            created_at=existing_diagram.created_at,
            updated_at=datetime.utcnow(),
            node_count=len(diagram.nodes),
            edge_count=len(diagram.edges)
        )
        self._diagram_store[diagram_id] = updated_diagram
        return updated_diagram
    
    def delete_diagram(self, diagram_id: int) -> None:
        """Delete a specific diagram."""
        if diagram_id not in self._diagram_store:
            raise ValueError(f"Diagram with ID {diagram_id} not found")
        del self._diagram_store[diagram_id]
    
    def add_node(self, diagram_id: int, node: NodeModel) -> Dict[str, Any]:
        """Add a node to a diagram."""
        if diagram_id not in self._diagram_store:
            raise ValueError(f"Diagram with ID {diagram_id} not found")
        
        diagram = self._diagram_store[diagram_id]
        diagram.nodes.append(node)
        diagram.node_count = len(diagram.nodes)
        diagram.updated_at = datetime.utcnow()
        
        return {
            "message": "Node added successfully",
            "node": node.dict(),
            "diagram_id": diagram_id,
            "total_nodes": diagram.node_count
        }
    
    def add_edge(self, diagram_id: int, edge: EdgeModel) -> Dict[str, Any]:
        """Add an edge to a diagram."""
        if diagram_id not in self._diagram_store:
            raise ValueError(f"Diagram with ID {diagram_id} not found")
        
        diagram = self._diagram_store[diagram_id]
        
        # Check if source and target nodes exist
        node_labels = [node.label for node in diagram.nodes]
        if edge.source_node not in node_labels or edge.target_node not in node_labels:
            raise ValueError("Source or target node does not exist in the diagram")
        
        diagram.edges.append(edge)
        diagram.edge_count = len(diagram.edges)
        diagram.updated_at = datetime.utcnow()
        
        return {
            "message": "Edge added successfully",
            "edge": edge.dict(),
            "diagram_id": diagram_id,
            "total_edges": diagram.edge_count
        }
    
    def render_diagram(self, diagram_id: int, format: str = "svg") -> Dict[str, Any]:
        """Render a diagram in specified format."""
        if diagram_id not in self._diagram_store:
            raise ValueError(f"Diagram with ID {diagram_id} not found")
        
        diagram = self._diagram_store[diagram_id]
        
        if format.lower() == "svg":
            # Simple SVG representation
            svg_content = self._generate_svg(diagram)
            return {
                "format": "svg",
                "content": svg_content,
                "diagram_id": diagram_id,
                "rendered_at": datetime.utcnow().isoformat()
            }
        elif format.lower() == "json":
            return {
                "format": "json",
                "content": diagram.dict(),
                "diagram_id": diagram_id,
                "rendered_at": datetime.utcnow().isoformat()
            }
        else:
            return {
                "error": f"Unsupported format: {format}",
                "supported_formats": ["svg", "json"]
            }
    
    def get_templates(self) -> Dict[str, Any]:
        """Get available diagram templates."""
        return {
            "templates": [
                {
                    "name": "Simple Flowchart",
                    "type": DiagramType.FLOWCHART,
                    "description": "Basic flowchart with start, process, and end nodes",
                    "sample_nodes": 3,
                    "sample_edges": 2
                },
                {
                    "name": "Organization Chart",
                    "type": DiagramType.ORGANIZATIONAL,
                    "description": "Hierarchical organization structure",
                    "sample_nodes": 5,
                    "sample_edges": 4
                },
                {
                    "name": "Network Diagram",
                    "type": DiagramType.NETWORK,
                    "description": "Network topology visualization",
                    "sample_nodes": 4,
                    "sample_edges": 4
                },
                {
                    "name": "Mind Map",
                    "type": DiagramType.MIND_MAP,
                    "description": "Central topic with branching ideas",
                    "sample_nodes": 6,
                    "sample_edges": 5
                }
            ]
        }
    
    def _generate_svg(self, diagram: DiagramResponse) -> str:
        """Generate a simple SVG representation of the diagram."""
        svg_elements = []
        svg_elements.append('<?xml version="1.0" encoding="UTF-8"?>')
        svg_elements.append('<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600" viewBox="0 0 800 600">')
        svg_elements.append(f'<title>{diagram.title}</title>')
        
        # Add nodes
        for node in diagram.nodes:
            if node.node_type.value == "rectangle":
                svg_elements.append(
                    f'<rect x="{node.x}" y="{node.y}" width="{node.width}" height="{node.height}" '
                    f'fill="{node.color}" stroke="{node.border_color}" stroke-width="2"/>'
                )
            elif node.node_type.value == "circle":
                radius = min(node.width, node.height) / 2
                cx = node.x + node.width / 2
                cy = node.y + node.height / 2
                svg_elements.append(
                    f'<circle cx="{cx}" cy="{cy}" r="{radius}" '
                    f'fill="{node.color}" stroke="{node.border_color}" stroke-width="2"/>'
                )
            
            # Add node label
            text_x = node.x + node.width / 2
            text_y = node.y + node.height / 2
            svg_elements.append(
                f'<text x="{text_x}" y="{text_y}" text-anchor="middle" dominant-baseline="middle" '
                f'font-family="Arial, sans-serif" font-size="12">{node.label}</text>'
            )
        
        # Add edges (simplified line connections)
        for edge in diagram.edges:
            source_node = next((n for n in diagram.nodes if n.label == edge.source_node), None)
            target_node = next((n for n in diagram.nodes if n.label == edge.target_node), None)
            
            if source_node and target_node:
                x1 = source_node.x + source_node.width / 2
                y1 = source_node.y + source_node.height / 2
                x2 = target_node.x + target_node.width / 2
                y2 = target_node.y + target_node.height / 2
                
                stroke_dasharray = "5,5" if edge.style == "dashed" else "none"
                svg_elements.append(
                    f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
                    f'stroke="{edge.color}" stroke-width="{edge.weight}" stroke-dasharray="{stroke_dasharray}"/>'
                )
                
                # Add edge label if present
                if edge.label:
                    label_x = (x1 + x2) / 2
                    label_y = (y1 + y2) / 2
                    svg_elements.append(
                        f'<text x="{label_x}" y="{label_y}" text-anchor="middle" '
                        f'font-family="Arial, sans-serif" font-size="10" fill="{edge.color}">{edge.label}</text>'
                    )
        
        svg_elements.append('</svg>')
        return '\n'.join(svg_elements)