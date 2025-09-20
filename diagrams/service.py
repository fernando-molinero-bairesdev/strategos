from diagrams.diagram import Diagram


class DiagramService:
    def __init__(self):
        self.diagrams = {}

    def create_diagram(self, diagram_data):
        diagram = Diagram.from_dict(diagram_data)
        self.diagrams[diagram.id] = diagram
        return diagram.to_dict()

    def get_diagram(self, diagram_id):
        diagram = self.diagrams.get(diagram_id)
        return diagram.to_dict() if diagram else None

    def update_diagram(self, diagram_id, diagram_data):
        if diagram_id in self.diagrams:
            self.diagrams[diagram_id] = Diagram.from_dict(diagram_data)
            return self.diagrams[diagram_id].to_dict()
        return None

    def delete_diagram(self, diagram_id):
        return self.diagrams.pop(diagram_id, None)

    def list_diagrams(self):
        return list(self.diagrams.values())
