from self_healing_visualizer.devices.charge import Charge
from self_healing_visualizer.devices.circuit_breaker import CircuitBreaker
from self_healing_visualizer.devices.generator import Generator
from self_healing_visualizer.devices.religator import Religator
from self_healing_visualizer.devices.wire import Wire
from self_healing_visualizer.devices.basic_device import GenericDevice
from self_healing_visualizer.interface.util import generate_UI
from self_healing_visualizer.enums.religator_state_enum import StateEnum
from self_healing_visualizer.enums.wire_state_enum import StateEnum as WireStateEnum
from self_healing_visualizer.enums.religator_source_enum import SourceEnum
from self_healing_visualizer.util.global_clock import GlobalClock, Scheduler


class CaseStudy:
    
    def __init__(self) -> None:
        self.matrix: list[list[GenericDevice]] = [
            [Generator(), Wire(WireStateEnum.NONE), CircuitBreaker(StateEnum.CLOSED), Wire(WireStateEnum.NONE), Charge(WireStateEnum.NONE), 
            Wire(WireStateEnum.NONE), Religator(StateEnum.CLOSED), Wire(WireStateEnum.NONE), Charge(WireStateEnum.NONE),
            Wire(WireStateEnum.NONE), Religator(StateEnum.OPEN), Wire(WireStateEnum.NONE), Charge(WireStateEnum.NONE),
            Wire(WireStateEnum.NONE), Religator(StateEnum.CLOSED),  Wire(WireStateEnum.NONE), Charge(WireStateEnum.NONE),
            Wire(WireStateEnum.NONE), CircuitBreaker(StateEnum.CLOSED), Wire(WireStateEnum.NONE), Generator()],

            [Generator(), Wire(WireStateEnum.NONE), CircuitBreaker(StateEnum.OPEN), Wire(WireStateEnum.NONE), Charge(WireStateEnum.NONE), 
            Wire(WireStateEnum.NONE), Religator(StateEnum.CLOSED), Wire(WireStateEnum.NONE)]
        ]

        self.matrix[0][0].connections = [None, self.matrix[0][1]]
        for x in range(1, len(self.matrix[0]) - 1):
            e = self.matrix[0][x]
            e.connections = [self.matrix[0][x - 1], self.matrix[0][x + 1]]
        self.matrix[0][-1].connections = [self.matrix[0][-2], None]

        self.matrix[1][0].connections = [None, self.matrix[1][1]]
        for x in range(1, len(self.matrix[1]) - 1):
            e = self.matrix[1][x]
            e.connections = [self.matrix[1][x - 1], self.matrix[1][x + 1]]
        self.matrix[1][-1].connections = [self.matrix[1][-2], self.matrix[0][7]]
        self.matrix[0][7].connections.append(self.matrix[1][-1])

        self.smart_grid_UI = generate_UI(self.matrix)

        GlobalClock.schedule(
            self.matrix[0][-2].observer,
            dt=0
        )(1, 0, self.matrix[0][-1], self.matrix[0][-1])

        GlobalClock.schedule(
            self.matrix[0][1].observer,
            dt=0
        )(1, 0, self.matrix[0][0], self.matrix[0][0])

        GlobalClock.schedule(
            self.matrix[1][1].observer,
            dt=0
        )(1, 0, self.matrix[1][0], self.matrix[1][0])

        self.faulty_wires_waves: list[list[int, int]] = [
            [[0, 5]], [[0, -4]]
        ]
    
    