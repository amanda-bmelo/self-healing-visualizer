from pygame import Surface, draw as py_draw, SRCALPHA
from self_healing_visualizer.devices.charge import Charge
from self_healing_visualizer.devices_interface.base import BaseUI
from self_healing_visualizer.devices_interface.wireUI import WireUI

class ChargeTriangle:
    """Simple utility class to help create the base Religator image"""
    state_colors = WireUI.colors
    @classmethod
    def surface(cls, size: int, state: int):
        s = Surface((size, size), SRCALPHA, 32)
        s.set_colorkey((0,0,0))
        py_draw.polygon(s, ChargeTriangle.state_colors[state], [(0, size), (size/2, 0), (size, size)])
        return s

class ChargeUI(WireUI):
    images = [
        ChargeTriangle.surface(30, 0),
        ChargeTriangle.surface(30, 1),
        ChargeTriangle.surface(30, 2)
    ]

    @property
    def state(self):
        return self.attached_element.state

    def surface(self) -> Surface:
        return ChargeUI.images[self.state]

    def draw(self, source_surface: Surface, dx=0, dy=0):
        return BaseUI.draw(self, source_surface, dx, dy)