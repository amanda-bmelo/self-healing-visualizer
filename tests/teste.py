from self_healing_visualizer.devices_interface.mainUI import MainUI
from self_healing_visualizer.devices_interface.substationUI import SubstationUI
from self_healing_visualizer.devices_interface.religatorUI import ReligatorUI, Religator
from self_healing_visualizer.devices_interface.wireUI import WireUI, Wire
from random import randint as rng


ui = {
    Religator: ReligatorUI,
    Wire: WireUI
}
y_spacing = 60
x_spacing = 60
y = 0

matrix = [
    [Religator(True, 10.0, 10.0), Wire(True, 10.0, 10.0, []), Religator(True, 10.0, 10.0), Wire(True, 10.0, 10.0, []), Religator(True, 10.0, 10.0)],
    [Religator(True, 10.0, 10.0), Wire(True, 10.0, 10.0, []), Wire(True, 10.0, 10.0, []), Wire(True, 10.0, 10.0, []), Religator(True, 10.0, 10.0)],
]

ui_matrix = []
y = 0
for line in matrix:
    x = 0
    new_line = []
    for element in line:
        new_line.append(
            ui[type(element)](element, x*x_spacing, y*y_spacing)
        )
        if isinstance(element, Wire):
            element.elements = [matrix[y][x-1], matrix[y][x+1]]
        x+=1
    ui_matrix.append(new_line)
    y+=1
matrix[1][2].elements.append(matrix[0][2])

subt = SubstationUI(-200, 0, ui_matrix)

mui = MainUI(
    600, 600,
    [subt]
)

[print(x) for x in ui_matrix]

while(1):
    mui.run()
    for line in subt.elements:
        for e in line:
            e.attached_element.state = [e.attached_element.state, not e.attached_element.state][rng(0,30) == 0]