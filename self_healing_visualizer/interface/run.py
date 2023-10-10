from time import sleep
from self_healing_visualizer.devices_interface.mainUI import MainUI
from self_healing_visualizer.case_study3 import *
from self_healing_visualizer.util.global_clock import GlobalClock

def update(mui, delay):
    mui.run()
    sleep(delay)

def run_UI(sub_ts: list["CaseStudy"]):
    mui = MainUI(
        900, 300,
        sub_ts
    )

    mui.run()
    for wave in sub_ts[0].faulty_wires_waves:
        GlobalClock.run_all_batches(
            lambda gc: 0
        )
        mui.run()
        sleep(1.3)
        for faulty_wire in wave:
            y,x = faulty_wire
            sub_ts[0].matrix[y][x].fault(None)
        mui.run()
        sleep(1.3)
        GlobalClock.run_all_batches(
            lambda gc: 0
        )
        mui.run()
        sleep(1)
    while(1):
        mui.run()
        


if __name__ == "__main__":
    cs = CaseStudy()
    run_UI([cs])
