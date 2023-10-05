from pygame import Surface
# from self_healing_visualizer.case_study1 import CaseStudy # Circular import
from self_healing_visualizer.devices_interface.wireUI import WireUI
from .base import BaseUI


class SmartGridUI(BaseUI):
    """Mother class to Handle group logic for drawing"""
    def __init__(self, x: float, y: float, elements: list["BaseUI"]):
        super().__init__(x, y)

        self.elements = elements

    def input(self, keys):
        return

    def draw(self, source_surface: Surface, dx=0, dy=0):
        for element in self.elements:
            element.draw(source_surface, self.x + dx, self.y + dy)