from feedback.baseP import basePID
from influx_client import influx_interface  # , Point
import serial
import pumpParams as pParam
import receiveData as rData
from time import sleep

interval = 9000


def main():

    sleep(5)
    # Create instance of the P-Regulators
    ph_p_regulator = basePID(6, 8)
    tds_p_regulator = basePID(550, 950)

    # Create structures for opcode and received measurements
    opcode_struct = pParam.PumpParams(0, 0, 0, 0, 0)
    receive_struct = rData.ReceiveData()

    # Create serial interface for UART connection from Pi to Arduino
    ser = serial.Serial("/dev/cu.usbmodel14201", 115200)
    ser.reset_input_buffer()

    # Create interface for connection to influx
    influx = influx_interface()

    try:
        while True:

            if ser.in_waiting == 6:
                line = ser.read(6)
                receive_struct.unpack(line)

                point = influx.create_point(
                    "pH_sensor", "ph_sensor", "001", receive_struct.ph_value
                )
                point = influx.create_point(
                    "tds_sensor", "tds_sensor", "001", receive_struct.tds_value
                )
                point = influx.create_point(
                    "temp_sensor", "temp_sensor", "001", receive_struct.temp_value
                )

                ph_check = ph_p_regulator.regulate(receive_struct.ph_value)
                tds_check = tds_p_regulator.regulate(receive_struct.tds_value)

                if ph_check == 1:
                    opcode_struct.pump_ph_down = 1
                    opcode_struct.circular_pump = 1
                    # code = int(format(16, "b"))
                    # opcode_struct.opcode = opcode_struct.opcode | code
                elif ph_check == -1:
                    opcode_struct.pump_ph_up = 1
                    opcode_struct.circular_pump = 1
                    # code = int(format(8, "b"))
                    # opcode_struct.opcode = opcode_struct.opcode | code
                else:
                    opcode_struct.pump_ph_up = 0
                    opcode_struct.pump_ph_down = 0
                    opcode_struct.circular_pump = 0
                    # up = int(format(8, "b"))
                    # down = int(format(16, "b"))
                    # opcode_struct.opcode = opcode_struct.opcode & ~(up | down)

                if tds_check == -1:
                    opcode_struct.pump_a = 1
                    opcode_struct.pump_b = 1
                    opcode_struct.circular_pump = 1
                    # a = int(format(2, "b"))
                    # b = int(format(4, "b"))
                    # circ = int(format(32, "b"))
                    # opcode_struct.opcode = opcode_struct.opcode | (a | b | circ)
                else:
                    opcode_struct.pump_a = 0
                    opcode_struct.pump_b = 0
                    # a = int(format(2, "b"))
                    # b = int(format(4, "b"))
                    # opcode_struct.opcode = opcode_struct.opcode & ~(a | b)

                opcode = opcode_struct.pack()

                ser.write(opcode)

    except KeyboardInterrupt:
        ser.close()
        influx.write(point)


main()
# if __name__ == "__main__":
