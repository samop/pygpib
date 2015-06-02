from gpib import usb2gpib

A=usb2gpib.Gpib('/dev/ttyACM0',115200)
A.address(6)
A.settings()
A.auto(1)
#A.put("*IDN?")
A.close()

