from gpib import prologix
from gpib import dalton

A=prologix.Prologix('/dev/ttyUSB0')
A.settings()
A.address(24)
#A.write("*IDN?\n")
A.info()
#print (A.read())
A.close()

