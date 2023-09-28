from self_healing_visualizer.devices_interface.mainUI import MainUI
from self_healing_visualizer.devices_interface.substationUI import SubstationUI
from self_healing_visualizer.devices_interface.religatorUI import ReligatorUI, Religator

religs = [
    ReligatorUI(
        x*60, 0,
        Religator(x+1 == 3, 10.0, 10.0)
    )
    for x in range(4)
]
matrix = [
    religs
]

subt = SubstationUI(0, 0, matrix)

mui = MainUI(
    600, 600,
    [subt]
)

while(1):
    mui.run()