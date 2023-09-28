from pygame import Surface

class BaseUI:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def surface(self) -> Surface:
        return Surface((1,1))
    
    def coords(self, surface: Surface) -> tuple[int, int]:
        w,h = surface.get_size()
        return (-w/2,-h/2)
    
    def draw(self, source_surface: Surface, dx=0, dy=0):
        _s = self.surface()
        _x, _y = self.coords(_s)
        source_surface.blit(_s, (self.x + dx + _x, self.y + dy + _y))