from devices.religator import Religator
from devices.wire import Wire


class CaseStudy:
    
    def __init__(self) -> None:
        matrix = [
            [Religator(True, 10.0, 10.0), Wire(True, 10.0, 10.0, []), Religator(True, 10.0, 10.0), 
            Wire(True, 10.0, 10.0, []), Religator(True, 10.0, 10.0)]
        ]
    
    