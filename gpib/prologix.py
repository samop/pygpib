import serial

class Prologix:
    """This is a prologix usb2gpib python library for interfacing the gpib in controller mode"""

    def __init__(self, serial_port, speed=9600):
	"""Initialized with parameters: serial_port as string (e.g. "/dev/ttyUSB0") and optional speed parameter (default 9600 bps)"""
        self.serial_port=serial_port
        self.speed=speed
        self.connected=0
	self.automatic=0
        self.controller=1
        self.addr=0
	self.lastline=''
	self.connect()
	self.settings()

    def CheckError(self):
        self.write("SYST:ERR?\n")
        self.write("++read eoi\n")
        s = self.read(100)
        print s


    def connect(self):
	if(self.connected==0):
            self.serial_handle=serial.Serial(self.serial_port,self.speed, timeout=0.5)
            self.connected=1
        else:
            print("Already connected.")

    def settings(self):
        self.write("++mode 1\n")
        self.write("++auto " +str(self.automatic)+"\n")
        self.write("++eos 3\n") # do not append CR or LF to GPIB data
        self.write("++eoi 1\n") #assert EOI with last byte to indicate EO data

    def read(self,length_of_data=255):
        return self.serial_handle.read(length_of_data)

    def write(self,string):
        if(self.connected):
            self.serial_handle.write(string)
            print(string)
        else:
            print("Not issuing the command. Not connected.")

    def writeread(self,string="",length_of_data=255):
        self.write(string)
        self.write('++read eoi\n')
        return self.read(length_of_data)

#    def put(self,string):
#        if(self.connected):
#            self.serial_handle.write(unicode(command)+unicode('\n'))
#            print(unicode(command))
#	    if(self.automatic and internal==0):
#                print self.get()
#        else:
#            print("Not issuing the command. Not connected.")


    def auto(self, automatic=1):
        self.write('++auto '+str(automatic)+"\n")
        self.automatic=automatic
        return

    def address(self, addr='?'):
        self.write('++addr '+str(addr)+"\n")
        if(addr!='?'):
            self.addr=addr

    def close(self):
        if(self.connected==1):
	    self.serial_handle.close()
            self.connected=0
        else:
            print("Already disconnected.")

    def getMassive(self):
        f = open("plot.bin", "wb")
        while (1):
            s = self.serial_handle.read(1000)           
            if len(s) > 0:
                f.write(s)
            else:
                break
   

    def info(self):
        'Prints information on gpib device'
        print("Serial port used %s @%d\n\n", self.serial_port, self.speed)
	print("Connected: " + "true\n" if(self.connected) else "false\n")
 	print("Address:"+ str(self.addr))
	#temp=self.automatic
	#self.auto(1)
	data=self.writeread("*IDN?\n")
	#data=self.read()
	print("Device ID string returned by *IDN? :"+data)
	#self.auto(temp)
