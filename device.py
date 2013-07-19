import re
from datetime import datetime, timedelta
from serial import Serial, SerialException
from record import Record

class DeviceNotFoundError(Exception):
    pass

class InvalidHeader(Exception):
    def __init__(self, header):
        super(InvalidHeader, self).__init__(header)

class Device(object):
    _SERIAL_MAX = 50
    _SERIAL_PING_TIMEOUT = 0.1
    _SERIAL_TIMEOUT = 1
    _SERIAL_BAUDRATE = 115200

    def __init__(self):
        super(Device, self).__init__()
        self._socket = None
        self._find_device()

        print 'Found device on {0}'.format(self._socket.name)

    def pull_log(self):
        reader = self._get_log_line()

        now = self._get_rounded_time()
        offset, delta = self._parse_header(reader.next())
        now -= offset

        records = []
        for record_raw in reader:
            record = Record(int(record_raw), now)
            records.append(record)
            now -= delta

        return records

    def clear_log(self):
        self._socket.write('c')

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if self._socket:
            self._socket.close()

    def _find_device(self):
        for i in xrange(Device._SERIAL_MAX):
            try:
                with Serial(i, timeout=Device._SERIAL_PING_TIMEOUT, baudrate=Device._SERIAL_BAUDRATE) as s:
                    s.write('p')
                    if s.readline().strip() == 'P':
                        break
            except SerialException:
                pass
        else:
            raise DeviceNotFoundError()

        self._socket = Serial(i, timeout=Device._SERIAL_TIMEOUT, baudrate=Device._SERIAL_BAUDRATE)

    def _get_log_line(self):
        self._socket.write('r')
        while True:
            line = self._socket.readline().strip()
            if line == '==':
                return
            yield line

    def _parse_header(self, header):
        match = re.match(r'^@ (\d+) (\d+)$', header)
        if not match:
            raise InvalidHeader(header)

        offset = timedelta(minutes=int(match.group(1)))
        delta = timedelta(minutes=int(match.group(2)))

        return offset, delta

    def _get_rounded_time(self):
        """The time is rounded to the minute"""
        tm = datetime.now()
        tm = tm - timedelta(
                seconds=tm.second,
                microseconds=tm.microsecond)
        return tm
