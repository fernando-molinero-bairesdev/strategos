"""
Diagram package for Strategos.
Handles diagram creation, manipulation, and visualization operations.
"""

from fastapi import APIRouter
from .models import DiagramModel, DiagramResponse, NodeModel, EdgeModel
from .services import DiagramService

router = APIRouter()

# Initialize diagram service
diagram_service = DiagramService()


@router.get("/", response_model=dict)
async def get_diagram_info():
    """Get information about the diagram package."""
    return {
        "package": "diagram",
        "description": "Diagram creation and visualization operations",
        "endpoints": ["/diagrams", "/nodes", "/edges", "/render"]
    }


@router.get("/diagrams", response_model=list[DiagramResponse])
async def get_all_diagrams():
    """Get all diagrams."""
    return diagram_service.get_all_diagrams()


@router.post("/diagrams", response_model=DiagramResponse)
async def create_diagram(diagram: DiagramModel):
    """Create a new diagram."""
    return diagram_service.create_diagram(diagram)


@router.get("/diagrams/{diagram_id}", response_model=DiagramResponse)
async def get_diagram(diagram_id: int):
    """Get a specific diagram by ID."""
    return diagram_service.get_diagram(diagram_id)


@router.put("/diagrams/{diagram_id}", response_model=DiagramResponse)
async def update_diagram(diagram_id: int, diagram: DiagramModel):
    """Update a specific diagram."""
    return diagram_service.update_diagram(diagram_id, diagram)


@router.delete("/diagrams/{diagram_id}")
async def delete_diagram(diagram_id: int):
    """Delete a specific diagram."""
    diagram_service.delete_diagram(diagram_id)
    return {"message": f"Diagram {diagram_id} deleted successfully"}


@router.post("/diagrams/{diagram_id}/nodes", response_model=dict)
async def add_node(diagram_id: int, node: NodeModel):
    """Add a node to a diagram."""
    return diagram_service.add_node(diagram_id, node)


@router.post("/diagrams/{diagram_id}/edges", response_model=dict)
async def add_edge(diagram_id: int, edge: EdgeModel):
    """Add an edge to a diagram."""
    return diagram_service.add_edge(diagram_id, edge)


@router.get("/diagrams/{diagram_id}/render")
async def render_diagram(diagram_id: int, format: str = "svg"):
    """Render a diagram in specified format."""
    return diagram_service.render_diagram(diagram_id, format)


@router.get("/templates")
async def get_diagram_templates():
    """Get available diagram templates."""
    return diagram_service.get_templates()