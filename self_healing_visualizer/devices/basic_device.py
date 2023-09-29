
class GenericDevice:
    """Class to represent a generic device. Used for defining the behaviour each device must reproduce"""

    def __init__(
            self
    ) -> None:
        self.UI = None ## Link between Interface and Logic classes

    def fault(self, _from: "GenericDevice"):
        raise NotImplementedError()
    
    def propagate(self, _except: "GenericDevice"):
        raise NotImplementedError()
