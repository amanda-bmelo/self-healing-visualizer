
class Wire:
    """Class to represent connection between devices"""

    def __init__(
            self, state: bool, max_tension: float, max_frequency: float, elements: list
    ) -> None:
        self.state = state
        self.fault_detected: bool = False
        self.max_tension = max_tension
        self.max_frequency = max_frequency
        self.elements = elements

        self.UI = None

    def observer(self, tension: float, frequency: float):
        """Function to detect a fault"""
        if tension > self.max_tension or frequency > self.max_frequency:
            self.fault_detected = True
