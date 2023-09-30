from pygame import Surface, draw as py_draw
from self_healing_visualizer.devices.wire import Wire
from self_healing_visualizer.devices_interface.base import BaseUI


class WireUI(BaseUI):
    colors = [(80, 80, 10),(30, 30, 10),(70,20,30)]
    w = [4, 2]
    def __init__(self, wire: Wire, x: float, y: float) -> None:
        super().__init__(x, y)
        self.attached_element = wire
        wire.UI = self

    def __repr__(self) -> str:
        return f"<Wire[{self.attached_element.state}]: ({self.x}, {self.y})>"

    @property
    def state(self):
        return self.attached_element.state

    def draw(self, source_surface: Surface, dx=0, dy=0):
        s_pos = (self.x + dx, self.y + dy)
        color, width = WireUI.colors[self.state], WireUI.w[self.state]
        for element in self.attached_element.elements:
            ui_element: BaseUI = element.UI
            py_draw.line(source_surface, color, s_pos, (ui_element.x + dx, ui_element.y + dy), width)