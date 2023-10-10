from time import sleep
from self_healing_visualizer.devices_interface.mainUI import MainUI
from self_healing_visualizer.case_study2 import *
from self_healing_visualizer.util.global_clock import GlobalClock


def run_UI(sub_ts: list["CaseStudy"]):
    mui = MainUI(
        900, 300,
        sub_ts
    )

    mui.run()
    fns = []
    while(fns != [] or GlobalClock.next_batch != []):
        for fn in fns:
            fn()
        fns = GlobalClock.roll_next_batch()
        mui.run()
        sleep(1)

    sleep(1)
    mui.run()
    sub_ts[0].matrix[0][3].fault(None)
    fns = []
    mui.run()
    sleep(1)

    while(fns != [] or GlobalClock.next_batch != []):
        for fn in fns:
            fn()
        fns = GlobalClock.roll_next_batch()
        mui.run()
        sleep(1)
    while(1):
        mui.run()
        


if __name__ == "__main__":
    cs = CaseStudy()
    run_UI([cs])
