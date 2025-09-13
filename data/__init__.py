"""
Data package for Strategos.
Handles data management, processing, and storage operations.
"""

from fastapi import APIRouter
from .models import DataModel, DataResponse
from .services import DataService

router = APIRouter()

# Initialize data service
data_service = DataService()


@router.get("/", response_model=dict)
async def get_data_info():
    """Get information about the data package."""
    return {
        "package": "data",
        "description": "Data management and processing operations",
        "endpoints": ["/items", "/process", "/export"]
    }


@router.get("/items", response_model=list[DataResponse])
async def get_all_items():
    """Get all data items."""
    return data_service.get_all_items()


@router.post("/items", response_model=DataResponse)
async def create_item(item: DataModel):
    """Create a new data item."""
    return data_service.create_item(item)


@router.get("/items/{item_id}", response_model=DataResponse)
async def get_item(item_id: int):
    """Get a specific data item by ID."""
    return data_service.get_item(item_id)


@router.put("/items/{item_id}", response_model=DataResponse)
async def update_item(item_id: int, item: DataModel):
    """Update a specific data item."""
    return data_service.update_item(item_id, item)


@router.delete("/items/{item_id}")
async def delete_item(item_id: int):
    """Delete a specific data item."""
    data_service.delete_item(item_id)
    return {"message": f"Item {item_id} deleted successfully"}


@router.post("/process")
async def process_data(data: dict):
    """Process data with various operations."""
    return data_service.process_data(data)


@router.get("/export")
async def export_data(format: str = "json"):
    """Export data in specified format."""
    return data_service.export_data(format)