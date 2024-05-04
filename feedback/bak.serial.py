import pumpParams as pp
import receiveData as rs
import serial
import time

if __name__ == '__main__':
    # Create an instance of PumpParams with your desired values
    operation = 0x02
    params = pp.PumpParams(opcode=operation, pump_a=0x0000, pump_b=0x0002, pump_ph_up=300,
                        pump_ph_down=400, circular_pump=1)
    receive = rs.ReceiveData()

    # Pack the data into a byte string
    data = params.pack()
    ser = serial.Serial('/dev/cu.usbmodem14201', 115200)
    ser.reset_input_buffer()
    # Now 'data' contains the packed byte string ready to be sent over serial
    # print("This is from the Pi")
    # print(data)  # For demonstration
    # byte_representation = ' '.join([f'{byte:08b}' for byte in data])
    # print(byte_representation)

    try:
        # Keep reading bytes from the serial port
        while True:
            # ser.write(data)
            if ser.in_waiting == 6:
                t0 = time.time()
                line = ser.read(6)
                print(len(line))
                receive.unpack(line)
                receive.print()
                t1 = time.time()

                print(t1 - t0)
                # ser.reset_input_buffer()

            # Print the byte as an integer
            # print("Whole line: ", line)  # If using Python 3
            # # Convert the received byte to an integer
            # received_byte = int(line)

            # # Print the binary representation of the received byte
            # binary_representation = bin(received_byte)[2:].zfill(16)
            # print("Received byte (binary representation):", binary_representation)

    except KeyboardInterrupt:
        # Close the serial port when the program is interrupted (Ctrl+C)
        ser.close()
