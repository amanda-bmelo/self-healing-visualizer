from pygame import Surface

from self_healing_visualizer.devices_interface.wireUI import WireUI
from .base import BaseUI


class SubstationUI(BaseUI):
    def __init__(self, x: float, y: float, elements: list[list[BaseUI]]):
        super().__init__(x, y)
        _elements = []
        for e in elements:
            if isinstance(e, WireUI):
                _elements.insert(0, e)
            else:
                _elements.append(e)
        print(_elements)
        self.elements = _elements

    def draw(self, source_surface: Surface, dx=0, dy=0):
        for element in self.elements:
            element.draw(source_surface, self.x + dx, self.y + dy)