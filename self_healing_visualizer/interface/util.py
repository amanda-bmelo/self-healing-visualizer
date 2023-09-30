
from self_healing_visualizer.devices_interface.smart_gridUI import SmartGridUI
from self_healing_visualizer.devices_interface.religatorUI import ReligatorUI, Religator
from self_healing_visualizer.devices_interface.wireUI import WireUI, Wire
from self_healing_visualizer.devices.basic_device import GenericDevice
from random import randint as rng

def generate_UI(matrix: list[list[GenericDevice]]) -> SmartGridUI:
    ui = {
        Religator: ReligatorUI,
        Wire: WireUI, # TODO more classes
    }
    y_spacing = 60
    x_spacing = 60
    y = 0


    ui_elements = []
    y = 0
    for line in matrix:
        x = 0
        for element in line:
            ui_elements.append(
                ui[type(element)](element, x*x_spacing, y*y_spacing)
            )
            x+=1
        y+=1

    return SmartGridUI(-200, 0, ui_elements)