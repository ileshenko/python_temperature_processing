from device import Device, DeviceNotFoundError

def pull_log(filename):
    with Device() as device:
        records = device.pull_log()
        with open(filename, 'a') as output_file:
            for record in records:
                output_file.write(record.serialize() + '\n')

def main():
    try:
        log = pull_log('output.log')
    except DeviceNotFoundError:
        print 'Device not found'

if __name__ == '__main__':
    main()
