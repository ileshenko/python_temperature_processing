from device import Device, DeviceNotFoundError

def pull_log():
    with Device() as device:
        records = device.pull_log()
        for record in records:
            print record, record.serialize()

def main():
    try:
        log = pull_log()
    except DeviceNotFoundError:
        print 'Device not found'

if __name__ == '__main__':
    main()
