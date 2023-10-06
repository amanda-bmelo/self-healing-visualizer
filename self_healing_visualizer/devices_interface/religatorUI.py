from pygame import Surface
from self_healing_visualizer.devices.religator import Religator
from self_healing_visualizer.util.colors import MainColors
from .base import BaseUI


class ReligatorSquare:
    """Simple utility class to help create the base Religator image"""
    state_colors = [MainColors.RED, MainColors.GREEN]
    @classmethod
    def surface(cls, size: int, state: int):
        s = Surface((size, size))
        s.fill(ReligatorSquare.state_colors[state])
        return s
    

class ReligatorUI(BaseUI):
    """Class to present Religator to the interface. Uses `Religator.state` to define which image to draw"""
    images = [
        ReligatorSquare.surface(30, 0),
        ReligatorSquare.surface(30, 1)
    ]
    def __init__(self, religator: Religator, x: float, y: float):
        super().__init__(x, y)
        self.attached_element = religator
        religator.UI = self

    @property
    def state(self):
        return self.attached_element.state

    def __repr__(self) -> str:
        return f"<ReligatorUI[{self.state}]: ({self.x}, {self.y})>"

    def surface(self) -> Surface:
        return ReligatorUI.images[self.state]