from gpib import prologix

A=prologix.Prologix('/dev/ttyUSB0')
A.settings()
A.address(6)
A.auto(1)
A.write("++eos 2\n")
A.write("*IDN?\n")
print (A.read())
A.CheckError()
A.close()

