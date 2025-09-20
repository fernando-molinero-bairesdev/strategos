from .base import BaseTemplate

class CircleTemplate(BaseTemplate):
    def draw(self, **kwargs) -> str:
        cx = kwargs.get("x", 0)
        cy = kwargs.get("y", 0)
        r = kwargs.get("size", 10)
        label = kwargs.get("label", "")
        return f'''
            <g transform="translate({cx - r}, {cy - r})">
                <circle cx="{r}" cy="{r}" r="{r}" fill="#f1f1f1" stroke="#333" />
                <text x="{-(len(label))}" y="{r + 20}" dominant-baseline="middle" text-anchor="middle" font-family="Arial" font-size="14">{label}</text>
            </g>
        '''

class LineTemplate(BaseTemplate):
    def draw(self, **kwargs) -> str:
        x1 = kwargs.get("x1", 0)
        y1 = kwargs.get("y1", 0)
        x2 = kwargs.get("x2", 100)
        y2 = kwargs.get("y2", 100)
        return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#333" stroke-width="2" marker-end="url(#arrowhead)" />'
