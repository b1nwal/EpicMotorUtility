import serial
import time

p = serial.Serial('COM4')
time.sleep(1)

class Component:
    def __init__(self, ID: str):
        self.ID = ID
        self.state = 0
    def write(self,x: int):
        self.state = x
        self.actuate("W",x=x)
    def actuate(self, command: str, x: int=""):
        p.write('{COMMAND} {ID} {X}'.format(COMMAND=command, ID=self.ID, X=x).encode('utf-8'))

class DCMotor(Component):
    def __init__(self, ID):
        super().__init__(ID)

m = DCMotor('MX0')

m.write(90)