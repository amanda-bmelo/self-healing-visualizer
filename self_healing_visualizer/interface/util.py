
from self_healing_visualizer.devices.basic_device import GenericDevice
from self_healing_visualizer.devices_interface.smart_gridUI import SmartGridUI
from random import randint as rng

def generate_UI(matrix: list[list[GenericDevice]]) -> SmartGridUI:
    from self_healing_visualizer.devices_interface.religatorUI import ReligatorUI, Religator
    from self_healing_visualizer.devices_interface.wireUI import WireUI, Wire
    from self_healing_visualizer.devices_interface.circuit_breakerUI import CircuitBreaker, CircuitBreakerUI
    from self_healing_visualizer.devices_interface.chargeUI import Charge, ChargeUI
    ui = {
        Religator: ReligatorUI,
        Wire: WireUI,
        CircuitBreaker: CircuitBreakerUI,
        Charge: ChargeUI,
    }
    y_spacing = 20
    x_spacing = 20
    y = 0


    ui_elements = []
    y = 0
    for line in matrix:
        x = 0
        for element in line:
            e = ui[type(element)](element, x, y)
            if type(e) == WireUI:
                ui_elements.insert(
                    0, e
                )
            else:
                ui_elements.append(
                    e
                )
            s_w = e.surface()
            s_w = s_w.get_width() if s_w != None else 0
            x+=x_spacing + s_w
        y+=y_spacing

    return SmartGridUI(-200, 0, ui_elements)