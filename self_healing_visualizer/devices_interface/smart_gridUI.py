from pygame import Surface
from case_study1 import CaseStudy
from self_healing_visualizer.devices_interface.wireUI import WireUI
from .base import BaseUI


class SmartGridUI(BaseUI):
    """Mother class to Handle group logic for drawing"""
    def __init__(self, x: float, y: float, case_studies: list[CaseStudy]):
        super().__init__(x, y)

        self.case_studies = case_studies
        self.index = 0

    @property
    def elements(self):
        return self.case_studies[self.index]

    def input(self, keys):
        return

    def draw(self, source_surface: Surface, dx=0, dy=0):
        for element in self.elements:
            element.draw(source_surface, self.x + dx, self.y + dy)