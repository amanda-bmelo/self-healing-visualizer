from pygame import Surface
from self_healing_visualizer.devices.circuit_breaker import CircuitBreaker
from .base import BaseUI


class CircuitBreakerSquare:
    """Simple utility class to help create the base CircuitBreaker image"""
    state_colors = [(90,10,20), (10,80,30)]
    @classmethod
    def surface(cls, size: int, state: int):
        s = Surface((size, size))
        s.fill(CircuitBreakerSquare.state_colors[state])
        return s
    

class CircuitBreakerUI(BaseUI):
    """Class to present CircuitBreaker to the interface. Uses `CircuitBreaker.state` to define which image to draw"""
    images = [
        CircuitBreakerSquare.surface(30, 0),
        CircuitBreakerSquare.surface(30, 1)
    ]
    def __init__(self, circuit_breaker: CircuitBreaker, x: float, y: float):
        super().__init__(x, y)
        self.attached_element = circuit_breaker
        circuit_breaker.UI = self

    @property
    def state(self):
        return self.attached_element.state

    def __repr__(self) -> str:
        return f"<CircuitBreakerUI[{self.state}]: ({self.x}, {self.y})>"

    def surface(self) -> Surface:
        return CircuitBreakerUI.images[self.state]