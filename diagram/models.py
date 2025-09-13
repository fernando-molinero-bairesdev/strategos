"""
Diagram models for the diagram package.
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum


class DiagramType(str, Enum):
    """Supported diagram types."""
    FLOWCHART = "flowchart"
    UML = "uml"
    NETWORK = "network"
    ORGANIZATIONAL = "organizational"
    MIND_MAP = "mind_map"


class NodeType(str, Enum):
    """Supported node types."""
    RECTANGLE = "rectangle"
    CIRCLE = "circle"
    DIAMOND = "diamond"
    ELLIPSE = "ellipse"
    HEXAGON = "hexagon"


class NodeModel(BaseModel):
    """Model for diagram nodes."""
    label: str = Field(..., description="Label text for the node")
    node_type: NodeType = Field(NodeType.RECTANGLE, description="Type of the node")
    x: float = Field(0.0, description="X coordinate position")
    y: float = Field(0.0, description="Y coordinate position")
    width: float = Field(100.0, description="Width of the node")
    height: float = Field(50.0, description="Height of the node")
    color: Optional[str] = Field("#ffffff", description="Background color of the node")
    border_color: Optional[str] = Field("#000000", description="Border color of the node")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional node metadata")


class EdgeModel(BaseModel):
    """Model for diagram edges."""
    source_node: str = Field(..., description="ID of the source node")
    target_node: str = Field(..., description="ID of the target node")
    label: Optional[str] = Field(None, description="Label for the edge")
    style: str = Field("solid", description="Edge style (solid, dashed, dotted)")
    color: str = Field("#000000", description="Color of the edge")
    weight: float = Field(1.0, description="Weight/thickness of the edge")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional edge metadata")


class DiagramModel(BaseModel):
    """Base model for diagrams."""
    title: str = Field(..., description="Title of the diagram")
    diagram_type: DiagramType = Field(DiagramType.FLOWCHART, description="Type of diagram")
    description: Optional[str] = Field(None, description="Description of the diagram")
    nodes: List[NodeModel] = Field(default_factory=list, description="List of nodes in the diagram")
    edges: List[EdgeModel] = Field(default_factory=list, description="List of edges in the diagram")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional diagram metadata")


class DiagramResponse(BaseModel):
    """Response model for diagram operations."""
    id: int = Field(..., description="Unique identifier for the diagram")
    title: str = Field(..., description="Title of the diagram")
    diagram_type: DiagramType = Field(..., description="Type of diagram")
    description: Optional[str] = Field(None, description="Description of the diagram")
    nodes: List[NodeModel] = Field(default_factory=list, description="List of nodes in the diagram")
    edges: List[EdgeModel] = Field(default_factory=list, description="List of edges in the diagram")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional diagram metadata")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")
    node_count: int = Field(..., description="Number of nodes in the diagram")
    edge_count: int = Field(..., description="Number of edges in the diagram")