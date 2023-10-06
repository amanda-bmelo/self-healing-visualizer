from time import sleep
from self_healing_visualizer.devices_interface.mainUI import MainUI
from self_healing_visualizer.case_study1 import *
from self_healing_visualizer.util.global_clock import GlobalClock


def run_UI(sub_ts: list["CaseStudy"]):
    mui = MainUI(
        1000, 600,
        sub_ts
    )

    fns = GlobalClock.roll_next_batch()
    while(fns != [] or GlobalClock.next_batch != []):
        for fn in fns:
            fn()
        fns = GlobalClock.roll_next_batch()
        mui.run()
    sub_ts[0].matrix[0][1].fault(None)
    fns = GlobalClock.roll_next_batch()
    sleep(0.4)
    while(fns != [] or GlobalClock.next_batch != []):
        for fn in fns:
            fn()
        fns = GlobalClock.roll_next_batch()
        mui.run()
        sleep(0.5)
    sleep(3)
    # while(1):
    #     mui.run()
        


if __name__ == "__main__":
    cs = CaseStudy()
    run_UI([cs])
