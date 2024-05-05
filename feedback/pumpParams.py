import struct

class PumpParams:
    def __init__(self, pump_a, pump_b, pump_ph_up, pump_ph_down, circular_pump):
        self.pump_a = pump_a
        self.pump_b = pump_b
        self.pump_ph_up = pump_ph_up
        self.pump_ph_down = pump_ph_down
        self.circular_pump = circular_pump

    def pack(self):
        return struct.pack('<BBBBB', self.pump_a, self.pump_b,
                           self.pump_ph_up, self.pump_ph_down, self.circular_pump)

    def pack_opcode(self):
        return struct.pack('<B', self.opcode)