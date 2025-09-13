"""
Data models for the data package.
"""

from pydantic import BaseModel, Field
from typing import Optional, Any
from datetime import datetime


class DataModel(BaseModel):
    """Base model for data items."""
    name: str = Field(..., description="Name of the data item")
    content: Any = Field(..., description="Content of the data item")
    description: Optional[str] = Field(None, description="Description of the data item")
    tags: Optional[list[str]] = Field(default_factory=list, description="Tags for the data item")


class DataResponse(BaseModel):
    """Response model for data operations."""
    id: int = Field(..., description="Unique identifier for the data item")
    name: str = Field(..., description="Name of the data item")
    content: Any = Field(..., description="Content of the data item")
    description: Optional[str] = Field(None, description="Description of the data item")
    tags: list[str] = Field(default_factory=list, description="Tags for the data item")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")


class ProcessingRequest(BaseModel):
    """Model for data processing requests."""
    operation: str = Field(..., description="Type of processing operation")
    parameters: dict = Field(default_factory=dict, description="Processing parameters")
    data: Any = Field(..., description="Data to be processed")