from gpib import prologix
from gpib import dalton

A=dalton.Dalton('/dev/ttyACM0')
A.settings()
A.address(24)
A.auto(1)
#A.write("*IDN?\n")
A.info()
#print (A.read())
A.close()

