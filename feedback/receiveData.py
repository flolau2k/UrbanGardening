import struct

class ReceiveData:
    def __init__(self):
        self.ph_value = 0
        self.tds_value = 0
        self.temp_value = 0

    def unpack(self, buffer):
        self.ph_value, self.tds_value, self.temp_value = struct.unpack('<HHH', buffer)

    def print(self):
        print(f"pH: {self.ph_value}, tds: {self.tds_value}, temp: {self.temp_value}")