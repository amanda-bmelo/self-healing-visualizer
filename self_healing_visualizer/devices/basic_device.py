
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
    
    def propagate(self, _except: "GenericDevice"):
        """Function to propagate the state of the device"""
        raise NotImplementedError()
