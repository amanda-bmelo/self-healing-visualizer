from self_healing_visualizer.devices.basic_device import GenericDevice
from self_healing_visualizer.enums.religator_source_enum import SourceEnum
from self_healing_visualizer.devices.wire import Wire


class Religator(GenericDevice):
    """Class to represent smart religators"""

    def __init__(
        self, state: bool
    ) -> None:
        super().__init__()
        self.state = state
        self.fault_detected = SourceEnum.NONE
        self.source = SourceEnum.NONE

    def observer(self, energy: bool, fault: bool, source: Wire):
        """Function to update the current state"""
        
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
            if self.source == direction and self.source != SourceEnum.NONE:
                self.source -= direction
                was_updated = True
            

        if self.source == SourceEnum.BOTH or self.fault_detected > 0 and self.state != 1:
            self.state = 1
            was_updated = True
        elif self.source in [1,2] and self.fault_detected == SourceEnum.NONE and self.state == 1:
            self.state = 0
            was_updated = True
        if was_updated:
            self.propagate()
            
    def propagate(self):
        """Function to propagate the state of the religator"""
        
        if self.state == 0:
            if self.source == SourceEnum.RIGHT:
                self.connections[SourceEnum.LEFT - 1].observer(self.energized, self.fault_detected > 0, self)
            elif self.source == SourceEnum.LEFT:
                self.connections[SourceEnum.RIGHT - 1].observer(self.energized, self.fault_detected > 0, self)
            else:
                raise Exception("Religator had state 0 when its enum source was set to both")
        else:
            for con in self.connections:
                con.observer(0, self.fault_detected > 0, self)
        