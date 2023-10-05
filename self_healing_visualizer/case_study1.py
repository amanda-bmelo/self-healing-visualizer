from self_healing_visualizer.devices.charge import Charge
from self_healing_visualizer.devices.circuit_breaker import CircuitBreaker
from self_healing_visualizer.devices.religator import Religator
from self_healing_visualizer.devices.wire import Wire
from self_healing_visualizer.interface.util import generate_UI


class CaseStudy:
    
    def __init__(self) -> None:
        self.matrix = [
            [CircuitBreaker(True), Wire(True), Charge(True), 
            Wire(True), Religator(True), Wire(True), Charge(True),
            Wire(True), Religator(True), Wire(True), Charge(True),
            Wire(True), Religator(True),  Wire(True), Charge(True),
            Wire(True), CircuitBreaker(True)]
        ]

        self.smart_grid_UI = generate_UI(self.matrix)

        self.faulty_wire = []
    
    