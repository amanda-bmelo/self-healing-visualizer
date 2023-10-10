from pygame import Surface, draw as py_draw, SRCALPHA
from self_healing_visualizer.devices.generator import Generator
from self_healing_visualizer.devices_interface.base import BaseUI
from self_healing_visualizer.util.colors import MainColors


class GeneratorCircle:
    """Simple utility class to help create the base Religator image"""
    state_colors = MainColors.YELLOW
    @classmethod
    def surface(cls, size: int, state: int):
        s = Surface((size, size), SRCALPHA, 32)
        s.set_colorkey((0,0,0))
        py_draw.circle(s, GeneratorCircle.state_colors, center=(size/2, size/2), radius=size/2)
        return s

class GeneratorUI(BaseUI):
    image = GeneratorCircle.surface(50, 0)
    colors = {}
    pre_made = [(251, 206, 177), (255, 191, 0), (253, 218, 13), (255, 255, 143), (223, 255, 0)]
    pre_made = [(216, 191, 216), (230, 230, 250), (207, 159, 255), (112, 41, 99), (170, 51, 106)]

    def __init__(self, generator: Generator, x: float, y: float) -> None:
        super().__init__(x, y)
        self.attached_element = generator
        generator.UI = self

        # x = len(GeneratorUI.colors) * 10 + 45
        # GeneratorUI.colors[generator.id] = (x*3 % 256, x*10 % 256, x*19 % 256)
        GeneratorUI.colors[generator.id] = GeneratorUI.pre_made[len(GeneratorUI.colors) % len(GeneratorUI.pre_made)]

    def surface(self) -> Surface:
        return GeneratorUI.image

    def draw(self, source_surface: Surface, dx=0, dy=0):
        return BaseUI.draw(self, source_surface, dx, dy)