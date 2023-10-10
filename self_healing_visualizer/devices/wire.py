from self_healing_visualizer.devices.basic_device import GenericDevice
from self_healing_visualizer.enums.wire_state_enum import StateEnum
from self_healing_visualizer.util.global_clock import GlobalClock
from self_healing_visualizer.util.print_function import print_entry

class Wire(GenericDevice):
    """Class to represent connection between devices"""

    def __init__(
            self, state: StateEnum
    ) -> None:
        super().__init__()
        self.state = state

    def observer(self, energy: bool, fault: bool, source: "GenericDevice"):
        """Function to update the current state"""
        new_state = energy if not fault else StateEnum.FAULT
        if new_state != self.state:
            self.state = new_state
            self.propagate(source)

    def fault(self, _from=None):
        self.state = StateEnum.FAULT
        self.propagate(_from)

    def propagate(self, _except: GenericDevice):
        """Function to propagate the state of the wire"""

        if _except == None:
            target_devices = self.connections
        else:
            target = self.connections.index(_except)
            target_devices = self.connections[:]
            target_devices.pop(target)
        if self.state == StateEnum.NONE:
            for td in target_devices:
                if td != None:
                    td.observer(0, 0, self)
        elif self.state == StateEnum.ENERGY:
            for td in target_devices:
                if td != None:
                    td.observer(1, 0, self)
        elif self.state == StateEnum.FAULT:
            for td in target_devices:
                if td != None:
                    td.observer(0, 1, self)
