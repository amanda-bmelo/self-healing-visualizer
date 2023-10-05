from self_healing_visualizer.devices.charge import Charge
from self_healing_visualizer.devices.circuit_breaker import CircuitBreaker
from self_healing_visualizer.devices.religator import Religator
from self_healing_visualizer.devices.wire import Wire
from self_healing_visualizer.devices.basic_device import GenericDevice
from self_healing_visualizer.interface.util import generate_UI
from self_healing_visualizer.enums.state import State


class CaseStudy:
    
    def __init__(self) -> None:
        self.matrix: list[list[GenericDevice]] = [
            [CircuitBreaker(State.CLOSED), Wire(State.CLOSED), Charge(State.CLOSED), 
            Wire(State.CLOSED), Religator(State.CLOSED), Wire(State.CLOSED), Charge(State.CLOSED),
            Wire(State.CLOSED), Religator(State.CLOSED), Wire(State.CLOSED), Charge(State.CLOSED),
            Wire(State.CLOSED), Religator(State.OPEN),  Wire(State.CLOSED), Charge(State.CLOSED),
            Wire(State.CLOSED), CircuitBreaker(State.CLOSED)]
        ]

        self.matrix[0][0].connections = self.matrix[0][1]
        for x in range(1, len(self.matrix[0]) - 1):
            e = self.matrix[0][x]
            e.connections = [self.matrix[0][x - 1], self.matrix[0][x + 1]]
        self.matrix[0][-1].connections = self.matrix[0][-2]

        self.smart_grid_UI = generate_UI(self.matrix)

        self.faulty_wire = []
    
    