import sys
from urllib2 import Request, urlopen
from urllib import urlencode

SOURCE = 'temperature.log'
API = 'http://spy.igor.leshenko.net'

def get_url(location):
    return API + '/' + location

def get_records():
    results = []
    with open(SOURCE, 'r') as log:
        for line in log.readlines():
            time, temperature = line.split()
            results.append(temperature + ':' + time)
    return ','.join(results)

def main():
    if len(sys.argv) != 2:
        print 'Usage: {0} location-name'.format(sys.argv[0])
        return
    location = sys.argv[1]

    data = {
            'records': get_records()
            }

    request = Request(get_url(location), urlencode(data))
    response = urlopen(request)
    if response.read().strip() == 'OK':
        open(SOURCE, 'w').truncate()

if __name__ == '__main__':
    main()
