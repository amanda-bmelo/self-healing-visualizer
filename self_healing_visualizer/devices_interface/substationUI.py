from pygame import Surface
from .base import BaseUI


class SubstationUI(BaseUI):
    def __init__(self, x: float, y: float, elements: list[list[BaseUI]]):
        super().__init__(x, y)
        self.elements = elements

    def draw(self, source_surface: Surface, dx=0, dy=0):
        for element_row in self.elements:
            for element in element_row:
                element.draw(source_surface, dx, dy)