import os
from datetime import datetime
from serial import Serial, SerialException

SERIAL_MAX= 50
SERIAL_TIMEOUT = 0.1
SERIAL_BAUDRATE = 115200

def find_device():
    """Iterates over com ports and ping everyone until get's ping
    from the real device. Returns a serial socket."""
    for i in xrange(SERIAL_MAX):
        device_found = False
        s = None
        try:
            s = Serial(i, timeout=SERIAL_TIMEOUT, baudrate=SERIAL_BAUDRATE)
            s.write('p')
            if s.readline().strip() == 'P':
                device_found = True
                return s
        except SerialException:
            pass
        finally:
            # If the device was found we can't destroy it because it's
            # returned from the function
            if not device_found and s:
                s.close()

def main():
    device = find_device()
    print device

if __name__ == '__main__':
    main()
