from self_healing_visualizer.devices.basic_device import GenericDevice

class Generator(GenericDevice):
    def observer(self, energy: bool, fault: bool, source: GenericDevice):
        pass

    def propagate(self, _except: GenericDevice):
        for elements in self.connections:
            if elements != None:
                elements.observer(1, 0, self)