from .registry import TemplateRegistry

registry = TemplateRegistry()

from . import shapes

registry.register("circle", shapes.CircleTemplate())
registry.register("line", shapes.LineTemplate())
