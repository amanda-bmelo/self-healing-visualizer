from self_healing_visualizer.devices.basic_device import GenericDevice
from self_healing_visualizer.enums.religator_source_enum import SourceEnum
from self_healing_visualizer.devices.wire import Wire
from self_healing_visualizer.util.global_clock import GlobalClock
from self_healing_visualizer.util.print_function import print_entry
from self_healing_visualizer.enums.religator_state_enum import StateEnum


class Religator(GenericDevice):
    """Class to represent smart religators"""

    def __init__(
        self, state: bool
    ) -> None:
        super().__init__()
        self.state = state
        self.fault_detected = SourceEnum.NONE
        self.source = SourceEnum.NONE
        self.generators = [None, None]

    def str(self) -> str:
        state = ['Closed', 'Open'][self.state]
        source = ['None', "Left", "Right", "Both"][self.source]
        fault_detected = ['None', "Left", "Right", "Both"][self.fault_detected]

        return f"<Religator[{self.id}]: ({state}, {source}, {fault_detected})>"
    
    def observer(self, energy: bool, fault: bool, source: Wire, generator: GenericDevice=None):
        self._observer(energy, fault, source)
        # if self.source != SourceEnum.BOTH and self.source != SourceEnum.NONE:
        #     self.generator = generator
        # else:
        #     self.generator = None
        direction = self.connections.index(source)
        self.generators[direction] = generator
        if self.state == StateEnum.CLOSED:
            self.update_state()
        else:
            GlobalClock.schedule(self.update_state)()

    def _observer(self, energy: bool, fault: bool, source: Wire):
        """Function to update the current state"""

        direction = self.connections.index(source) + 1
        if fault:
            if self.fault_detected != direction and self.fault_detected != SourceEnum.BOTH:
                self.fault_detected += direction
        
        if energy:
            if self.source != direction and self.source != SourceEnum.BOTH:
                self.source += direction
        else:
            if self.source == direction or self.source == SourceEnum.BOTH:
                self.source -= direction
            
    def update_state(self):
        if (self.source == SourceEnum.BOTH or self.fault_detected > 0):
            if self.state != StateEnum.OPEN:
                self.state = StateEnum.OPEN
        elif self.source in [1,2] and self.fault_detected == SourceEnum.NONE:
            if self.state != StateEnum.CLOSED:
                self.state = StateEnum.CLOSED

        self.propagate()
        
        if self.source == SourceEnum.NONE and self.fault_detected == SourceEnum.NONE:
            if self.state != StateEnum.OPEN:
                self.state = StateEnum.OPEN

    @GlobalClock.schedule
    def __propagate(self):
        return self.propagate()
    def propagate(self):
        """Function to propagate the state of the religator"""

        target = None
        direction = None
        target1 = None
        target2 = None
        if self.state == StateEnum.CLOSED:
            energy, fault = (1, 0)
            if self.source == SourceEnum.RIGHT:
                target = self.connections[SourceEnum.LEFT - 1]
                direction = SourceEnum.RIGHT - 1
            elif self.source == SourceEnum.LEFT:
                target = self.connections[SourceEnum.RIGHT - 1]
                direction = SourceEnum.LEFT - 1
            elif self.source == SourceEnum.NONE:
                energy, fault = (0, 0)
                target1 = self.connections[SourceEnum.RIGHT - 1]
                target2 = self.connections[SourceEnum.LEFT - 1]
                if target1 != None:
                    target1.observer(energy, fault, self, self.generators[SourceEnum.LEFT-1])
                if target2 != None:
                    target2.observer(energy, fault, self, self.generators[SourceEnum.RIGHT-1])
            else:
                raise Exception(f"{self.str()} had state 0 when its enum source was set to both")
        else:
            energy, fault = (0, 0)
            if self.fault_detected == SourceEnum.RIGHT and not (self.source == SourceEnum.LEFT or self.source == SourceEnum.BOTH):
                target = self.connections[SourceEnum.LEFT - 1]
                direction = SourceEnum.RIGHT - 1
            elif self.fault_detected == SourceEnum.LEFT and  not (self.source == SourceEnum.RIGHT or self.source == SourceEnum.BOTH):
                target = self.connections[SourceEnum.RIGHT - 1]
                direction = SourceEnum.LEFT - 1

        if target != None:
            target.observer(energy, fault, self, self.generators[direction])

        