import serial

class Gpib:
    'This is a simple usb2gpib python library for the interfacing the gpib'
    def __init__(self,serial_port,speed=115200):
        self.serial_port=serial_port
        self.speed=speed
        self.connected=0
	self.automatic=0
	self.lastline=''
	self.connect()
	self.settings()


    def info(self):
        'Prints information on gpib device'
        print("Serial port used %s @%d\n\n",self.serial_port, self.speed)
	print("Connected: " + "true\n" if(self.connected) else "false\n")
 
    def put(self, command, internal=0):
        'puts command to the remote machine'
        if(self.connected):
            self.serial_handle.write(unicode(command)+unicode('\n'))
            print(unicode(command))
	    if(self.automatic and internal==0):
                print self.get()
        else:
            print("Not issuing the command. Not connected.")

    def get(self):
        retval=self.serial_handle.readline()
        self.lastline=retval
        return retval

    def connect(self):
	if(self.connected==0):
            self.serial_handle=serial.Serial(self.serial_port,self.speed, timeout=1)
            self.connected=1
        else:
            print("Already connected.")

    def close(self):
        if(self.connected==1):
	    self.serial_handle.close()
            self.connected=0
        else:
            print("Already disconnected.")

    def address(self, addr='?'):
        self.put('++addr '+str(addr))

    def settings(self):
        self.put('++eoi 0',1)
        self.put('++eos 0',1)
        self.put('++eot 0',1)
	self.auto(1)

    def auto(self, automatic=1 ):
        "this sets the auto answer mode of the USB2GPIB interface. auto can be 0 or 1"
        self.put('++auto '+str(automatic),1)
        self.automatic=automatic
        return


