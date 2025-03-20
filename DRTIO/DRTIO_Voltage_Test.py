from artiq.experiment import *
import numpy as np

class DCVoltageControl(EnvExperiment):
    """DRTIO Voltage Test"""

    def build(self):
        self.setattr_device("core")
        self.setattr_device("spi_zotino1")
        self.setattr_device("ttl_zotino1_ldac")
        self.setattr_device("ttl_zotino1_clr")
        self.setattr_device("zotino1")

        self.setattr_argument("ch1", NumberValue(0.02, precision=3, step=.01, min=0.0, max=9.99))


    @kernel
    def run(self):
        self.core.reset()
        delay(1 * us)
        self.core.break_realtime()
        delay(1 * us)
        self.zotino1.init()
        delay(2 * ms)

        self.zotino1.write_dac(0, 2)
        delay(2*ms)
        self.zotino1.load()