from self_healing_visualizer.devices_interface.mainUI import MainUI
from self_healing_visualizer.devices_interface.substationUI import SubstationUI
from self_healing_visualizer.devices_interface.religatorUI import ReligatorUI, Religator
from self_healing_visualizer.devices_interface.wireUI import WireUI, Wire
from self_healing_visualizer.devices.basic_device import GenericDevice
from random import randint as rng

def generate_UI(matrix: list[GenericDevice]) -> SubstationUI:
    ui = {
        Religator: ReligatorUI,
        Wire: WireUI
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
    matrix[1][2].elements.append(matrix[0][2])

    return SubstationUI(-200, 0, ui_elements)

def run_UI(sub_ts: list[SubstationUI]):
    mui = MainUI(
        600, 600,
        sub_ts
    )

    while(1):
        mui.run()