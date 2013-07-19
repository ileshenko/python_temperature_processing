import os
from device import Device, DeviceNotFoundError

def pull_log():
    with Device() as device:
        print device
        print device.pull_log()

def main():
    try:
        log = pull_log()
    except DeviceNotFoundError:
        print 'Device not found'

if __name__ == '__main__':
    main()
