from datetime import datetime
from serial import Serial, SerialException

class DeviceNotFoundError(Exception):
    pass

class Device(object):
    _SERIAL_MAX= 50
    _SERIAL_TIMEOUT = 0.1
    _SERIAL_BAUDRATE = 115200

    def __init__(self):
        super(Device, self).__init__()
        self._socket = None

        self._find_device()

    def pull_log(self):
        pass

    def clear_log(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if self._socket:
            self._socket.close()

    def _find_device(self):
        for i in xrange(Device._SERIAL_MAX):
            try:
                with Serial(i, timeout=Device._SERIAL_TIMEOUT, baudrate=Device._SERIAL_BAUDRATE) as s:
                    s.write('p')
                    if s.readline().strip() == 'P':
                        break
            except SerialException:
                pass
        else:
            raise DeviceNotFoundError()

        self._socket = Serial(i, timeout=Device._SERIAL_TIMEOUT, baudrate=Device._SERIAL_BAUDRATE)
