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

    def str(self) -> str:
        state = ['Closed', 'Open'][self.state]
        source = ['None', "Left", "Right", "Both"][self.source]
        fault_detected = ['None', "Left", "Right", "Both"][self.fault_detected]

        return f"<Religator[{self.id}]: ({state}, {source}, {fault_detected})>"

    def observer(self, energy: bool, fault: bool, source: Wire):
        """Function to update the current state"""

        print(self.str(), ['no energy','energy'][energy], ['/ no fault','/ fault'][fault])

        was_updated = False
        direction = self.connections.index(source) + 1
        if fault:
            if self.fault_detected != direction and self.fault_detected != SourceEnum.BOTH:
                self.fault_detected += direction
                was_updated = True
        
        if energy:
            if self.source != direction and self.source != SourceEnum.BOTH:
                self.source += direction
                was_updated = True
        else:
            if self.source == direction or self.source == SourceEnum.BOTH:
                self.source -= direction
                was_updated = True
            

        if (self.source == SourceEnum.BOTH or self.fault_detected > 0) and self.state != 1:
            self.state = StateEnum.OPEN
            was_updated = True
        elif self.source in [1,2] and self.fault_detected == SourceEnum.NONE and self.state == 1:
            self.state = StateEnum.CLOSED
            was_updated = True

        if was_updated:
            self.propagate()

    @GlobalClock.schedule
    def propagate(self):
        """Function to propagate the state of the religator"""

        target = None
        target1 = None
        target2 = None
        if self.state == StateEnum.CLOSED:
            energy, fault = (1, 0)
            if self.source == SourceEnum.RIGHT:
                target = self.connections[SourceEnum.LEFT - 1]
            elif self.source == SourceEnum.LEFT:
                target = self.connections[SourceEnum.RIGHT - 1]
            elif self.source == SourceEnum.NONE:
                energy, fault = (0, 0)
                target1 = self.connections[SourceEnum.RIGHT - 1]
                target2 = self.connections[SourceEnum.LEFT - 1]
                if target1 != None:
                    target1.observer(energy, fault, self)
                if target2 != None:
                    target2.observer(energy, fault, self)
            else:
                raise Exception(f"{self.str()} had state 0 when its enum source was set to both")
        else:
            energy, fault = (0, 0)
            if self.fault_detected == SourceEnum.RIGHT and not (self.source == SourceEnum.LEFT or self.source == SourceEnum.BOTH):
                target = self.connections[SourceEnum.LEFT - 1]
            elif self.fault_detected == SourceEnum.LEFT and  not (self.source == SourceEnum.RIGHT or self.source == SourceEnum.BOTH):
                target = self.connections[SourceEnum.RIGHT - 1]

        if target != None:
            target.observer(energy, fault, self)

        