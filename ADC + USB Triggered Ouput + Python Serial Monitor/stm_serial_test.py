
try:
    import serial
except ImportError:
    print('Pyserial not installed.')
    raise
import time
import threading
import sys

SERIAL_MSG_BYTES = 14*2
SERIAL_PORT = 'COM4'
SERIAL_BAUD = 9600

def serial_read_thread():
    i = True
    serial_stm.reset_output_buffer()
    serial_stm.write(bytes(b' '))
    while(True):
        msg_read = serial_stm.read(SERIAL_MSG_BYTES)
        print(msg_read)

if __name__ == "__main__" :
    serial_stm = serial.Serial(SERIAL_PORT,SERIAL_BAUD)
    time.sleep(1)
    th_1 = threading.Thread(target = serial_read_thread)

    th_1.start()
    time.sleep(1)

    serial_stm.close()
    sys.exit()