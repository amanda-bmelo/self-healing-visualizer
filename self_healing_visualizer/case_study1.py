from devices.charge import Charge
from devices.circuit_breaker import CircuitBreaker
from devices.religator import Religator
from devices.wire import Wire
from interface.run import run_UI


class CaseStudy:
    
    def __init__(self) -> None:
        self.matrix = [
            [CircuitBreaker(True), Wire(True), Charge(True), 
            Wire(True), Religator(True), Wire(True), Charge(True),
            Wire(True), Religator(True), Wire(True), Charge(True),
            Wire(True), Religator(True),  Wire(True), Charge(True),
            Wire(True), CircuitBreaker(True)]
        ]

        self.smart_grid_UI = run_UI.generate_UI(self.matrix)

        self.faulty_wire = []
    
    