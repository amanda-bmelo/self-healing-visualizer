from self_healing_visualizer.util.global_clock import GlobalClock


class GenericDevice:
    """Class to represent a generic device. Used for defining the behaviour each device must reproduce"""

    _id = 1
    @classmethod
    def next_id(cls):
        GenericDevice._id += 1
        return GenericDevice._id - 1

    def __init__(
            self
    ) -> None:
        self.id = GenericDevice.next_id()
        self.UI = None ## Link between Interface and Logic classes
        self.connections = []

    def observer(self, energy: bool, fault: bool, source: "GenericDevice"):
        """Function to update the current state"""
        raise NotImplementedError()

    def fault(self, _from: "GenericDevice"):
        """Function to set a fault on the device"""
        raise NotImplementedError()
    
    # @GlobalClock.schedule
    def propagate(self, _except: "GenericDevice"):
        """Function to propagate the state of the device"""
        raise NotImplementedError()
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}[{self.id}]: [{[f'{x.__class__.__name__}({x.id})' for x in self.connections if x != None]}]>"
    def str(self) -> str:
        return f"<{self.__class__.__name__}[{self.id}]>"