from fastapi import APIRouter, Depends
from diagrams.service import DiagramService


# This is a placeholder for your actual dependency provider.
# You would typically define this where you instantiate DiagramService.
def get_diagram_service():
    # This function should yield or return an instance of DiagramService
    # For example:
    # db = SessionLocal()
    # try:
    #     yield DiagramService(db)
    # finally:
    #     db.close()
    return DiagramService()


router = APIRouter(
    prefix="/diagrams",
    tags=["diagrams"],
)


@router.post("")
def create_diagram(diagram_service: DiagramService = Depends(get_diagram_service), diagram_data: dict = {}):
    return diagram_service.create_diagram(diagram_data)


@router.get("/{diagram_id}")
def get_diagram(diagram_id: str, diagram_service: DiagramService = Depends(get_diagram_service)):
    return diagram_service.get_diagram(diagram_id)


@router.put("/{diagram_id}")
def update_diagram(diagram_id: str, diagram_service: DiagramService = Depends(get_diagram_service), diagram_data: dict = {}):
    return diagram_service.update_diagram(diagram_id, diagram_data)


@router.delete("/{diagram_id}")
def delete_diagram(diagram_id: str, diagram_service: DiagramService = Depends(get_diagram_service)):
    return diagram_service.delete_diagram(diagram_id)


@router.get("")
def list_diagrams(diagram_service: DiagramService = Depends(get_diagram_service)):
    return diagram_service.list_diagrams()