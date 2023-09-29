from pygame import Surface

class BaseUI:
    """
    Basic class to show information on screen
    
    By default, it will draw `.surface()`'s (default is a 1x1 black Surface) result, into source_surface from `.draw(source_surface, ...)`, using `.coords(surface)`'s coordinate tuple (default to `(-w/2, -h/2)` from surface argument)

    ```py
    def draw(self, source_surface, ...):
        source_surface.blit(self.surface(), self.coords(self.surface()))
    ```
    """
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def surface(self) -> Surface:
        """Return the surface to be draw inside `.draw(...)`"""
        return Surface((1,1))
    
    def coords(self, surface: Surface) -> tuple[int, int]:
        """Returns `(x,y)` values for changing the entity's drawing anchor, where `(0,0)` means top left of it's `.surface(...)`"""
        w,h = surface.get_size()
        return (-w/2,-h/2)
    
    def draw(self, source_surface: Surface, dx=0, dy=0):
        # TODO One problem with `(dx, dy)` system is that a further down class' x and y attribute will be innacurate, since they don't aren't affected by their parent's x and y values. Propagation should be the correct method`
        _s = self.surface()
        _x, _y = self.coords(_s)
        source_surface.blit(_s, (self.x + dx + _x, self.y + dy + _y))