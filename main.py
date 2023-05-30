import serial

# Business Layer Logic

class EMU:
    pass

class Motor:
    def __init__(self, id):
        self.id = id

class Com:
    def __init__(self, port, rate=9600, motors=[], ):
