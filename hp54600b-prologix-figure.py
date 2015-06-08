from gpib import prologix

A=prologix.Prologix('/dev/ttyUSB0')
A.settings()
A.address(24)
A.auto(1)
#A.write("*IDN?\n")
#print (A.read())
A.getMassive()
A.close()

