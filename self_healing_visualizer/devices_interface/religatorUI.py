from pygame import Surface
from self_healing_visualizer.devices.religator import Religator
from .base import BaseUI


class ReligatorSquare:
    state_colors = [(90,10,20), (10,80,30)]
    @classmethod
    def surface(cls, size: int, state: int):
        s = Surface((size, size))
        s.fill(ReligatorSquare.state_colors[state])
        return s

class ReligatorUI(BaseUI):
    images = [
        ReligatorSquare.surface(30, 0),
        ReligatorSquare.surface(30, 1)
    ]
    def __init__(self, x: float, y: float, religator: Religator):
        super().__init__(x, y)
        self.religator = religator

    @property
    def state(self):
        return self.religator.state

    def __repr__(self) -> str:
        return f"<ReligatorUI[{self.state}]>"

    def surface(self) -> Surface:
        return ReligatorUI.images[self.state]