import serial
from .prologix import Prologix


class Dalton(Prologix):
    """The interface for the dalton.ax/gpib PIC based USB to GPIB controller. I've created a breadboard version of it. When using the firmware 2014-12-02, it acts almost as prologix controller. There is a slight change in the settings, so we are overriding them here"""
	
    def settings(self):
        """Overriding method for settings"""
	self.auto(self.automatic)
        self.write('++eoi 0\n')
        self.write('++eos 0\n')
        self.write('++eot 0\n')
	self.address(self.addr)

