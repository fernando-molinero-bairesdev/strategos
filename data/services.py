"""
Data services for the data package.
"""

from typing import List, Dict, Any
from datetime import datetime
from .models import DataModel, DataResponse


class DataService:
    """Service class for data operations."""
    
    def __init__(self):
        """Initialize the data service with in-memory storage."""
        self._data_store: Dict[int, DataResponse] = {}
        self._next_id = 1
    
    def get_all_items(self) -> List[DataResponse]:
        """Get all data items."""
        return list(self._data_store.values())
    
    def create_item(self, item: DataModel) -> DataResponse:
        """Create a new data item."""
        now = datetime.utcnow()
        data_response = DataResponse(
            id=self._next_id,
            name=item.name,
            content=item.content,
            description=item.description,
            tags=item.tags or [],
            created_at=now,
            updated_at=now
        )
        self._data_store[self._next_id] = data_response
        self._next_id += 1
        return data_response
    
    def get_item(self, item_id: int) -> DataResponse:
        """Get a specific data item by ID."""
        if item_id not in self._data_store:
            raise ValueError(f"Item with ID {item_id} not found")
        return self._data_store[item_id]
    
    def update_item(self, item_id: int, item: DataModel) -> DataResponse:
        """Update a specific data item."""
        if item_id not in self._data_store:
            raise ValueError(f"Item with ID {item_id} not found")
        
        existing_item = self._data_store[item_id]
        updated_item = DataResponse(
            id=existing_item.id,
            name=item.name,
            content=item.content,
            description=item.description,
            tags=item.tags or [],
            created_at=existing_item.created_at,
            updated_at=datetime.utcnow()
        )
        self._data_store[item_id] = updated_item
        return updated_item
    
    def delete_item(self, item_id: int) -> None:
        """Delete a specific data item."""
        if item_id not in self._data_store:
            raise ValueError(f"Item with ID {item_id} not found")
        del self._data_store[item_id]
    
    def process_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Process data with various operations."""
        operation = data.get("operation", "identity")
        content = data.get("content", {})
        
        if operation == "count":
            if isinstance(content, list):
                return {"result": len(content), "operation": operation}
            elif isinstance(content, dict):
                return {"result": len(content.keys()), "operation": operation}
            else:
                return {"result": 1, "operation": operation}
        
        elif operation == "transform":
            # Simple transformation example
            if isinstance(content, dict):
                return {
                    "result": {k.upper(): v for k, v in content.items()},
                    "operation": operation
                }
            return {"result": content, "operation": operation}
        
        else:
            # Identity operation
            return {"result": content, "operation": "identity"}
    
    def export_data(self, format: str = "json") -> Dict[str, Any]:
        """Export data in specified format."""
        if format.lower() == "json":
            return {
                "format": "json",
                "data": [item.dict() for item in self._data_store.values()],
                "count": len(self._data_store),
                "exported_at": datetime.utcnow().isoformat()
            }
        else:
            return {
                "error": f"Unsupported format: {format}",
                "supported_formats": ["json"]
            }