import os
from datetime import datetime
from serial import Serial, SerialException

SERIAL_MAX= 50
SERIAL_TIMEOUT = 0.1
SERIAL_BAUDRATE = 115200

class NoDeviceError(Exception):
    pass

def find_device():
    """Iterates over com ports and ping everyone until get's reply
    from the real device. Returns a serial socket."""
    for i in xrange(SERIAL_MAX):
        try:
            with Serial(i, timeout=SERIAL_TIMEOUT, baudrate=SERIAL_BAUDRATE) as s:
                s.write('p')
                if s.readline().strip() == 'P':
                    break
        except SerialException:
            pass
    else:
        raise NoDeviceError()

    return Serial(i, timeout=SERIAL_TIMEOUT, baudrate=SERIAL_BAUDRATE)

def pull_log():
    with find_device() as device:
        print device

def main():
    try:
        log = pull_log()
    except NoDeviceError:
        print 'Device not found'

if __name__ == '__main__':
    main()
