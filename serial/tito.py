import serial
import io

def auto(ser, auto ):
   "this sets the auto answer mode of the USB2GPIB interface"
   ser.write(unicode("++auto ")+str(auto)+unicode("\n"))
   return

ser=serial.Serial('/dev/ttyACM0',115200,timeout=1)
print ser.name
ser.write(unicode("\n"))
ser.write(unicode("++addr 2\n"))
ser.write(unicode("++auto 1\n"))
ser.write(unicode("++eoi 0\n"))
ser.write(unicode("++eos 0\n"))
ser.write(unicode("++eot 0\n"))
ser.write(unicode("++auto 1\n"))
ser.write(unicode("*IDN?\n"))
ret=ser.readline()
print ret
ser.write(unicode("++auto 0\n"))
ser.write(unicode("DISP:TEXT 'VSE_NAJ_TITO'\n"))
ser.write(unicode("DISP:WIND:MODE TEXT\n"))
ser.close()

