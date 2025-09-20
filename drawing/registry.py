from typing import Dict
from .base import BaseTemplate

class TemplateRegistry:
    def __init__(self):
        self._templates: Dict[str, BaseTemplate] = {}

    def register(self, name: str, template: BaseTemplate):
        self._templates[name] = template

    def get(self, name: str) -> BaseTemplate:
        return self._templates.get(name)
