import serial
import time

class EMU:
    def __init__(self):
        self.port = ''
        self.components = []
        self.com = ''

    def com(self,port,rate=9600):
        self.port = port
        self.com = serial.Serial(self.port,rate)
        time.sleep(1) # wait for arduino to catch up TODO have arduino respond instead
    def page(self,command: str, x):
        self.com.write(command.encode('utf-8'))
        self.com.write(self.id.encode('utf-8'))
        self.com.write(x.encode('utf-8'))

class Component:
    def __init__(self, ID: str, EMUInstance: EMU):
        self.EMUInstance = EMUInstance
        self.ID = ID
        self.state = 0
    def write(self,x: int):
        self.state = x
        self.EMUInstance.page("W",self.ID,self.state)

class ServoMotor(Component):
    def __init__(self, ID: str, EMUInstance: EMU):
        super().__init__(ID, EMUInstance)

e = EMU()
e.com('COM5',rate=4800)

ms0 = e.ServoMotor('MS0')