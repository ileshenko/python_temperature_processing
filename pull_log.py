from device import Device, DeviceNotFoundError

def pull_log(filename):
    with Device() as device:
        records = device.pull_log()
        records.sort()
        with open(filename, 'a') as output_file:
            for record in records:
                output_file.write(record.serialize() + '\n')

def main():
    try:
        pull_log('temperature.log')
    except DeviceNotFoundError:
        print 'Device not found'
    except IOError, error:
        print error

if __name__ == '__main__':
    main()
