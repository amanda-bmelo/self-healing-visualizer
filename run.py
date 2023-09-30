from self_healing_visualizer.devices_interface.mainUI import MainUI
from case_study1 import CaseStudy

def run_UI(sub_ts: list["CaseStudy"]):
    mui = MainUI(
        600, 600,
        sub_ts
    )

    while(1):
        mui.run()
        
        
if __name__ == "__main__":
    run_UI([CaseStudy])