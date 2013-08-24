import sys
import time

from urllib2 import Request, urlopen
from urllib import urlencode

SOURCE = 'temperature.log'
API = 'http://spy.igor.leshenko.net'

def get_url(location):
    return API + '/' + location

def get_records():
    offset = time.timezone if (time.localtime().tm_isdst == 0) else time.altzone
    results = []
    with open(SOURCE, 'r') as log:
        for line in log.readlines():
            gmt_time, temperature = line.split()
            local_time = int(gmt_time) - offset
            results.append(temperature + ':' + str(local_time))
    return ','.join(results)

def main():
    if len(sys.argv) != 2:
        raw_input( 'Usage: {0} location-name'.format(sys.argv[0]))

        return
    location = sys.argv[1]

    data = {
            'records': get_records()
            }

    request = Request(get_url(location), urlencode(data))
    response = urlopen(request)
    if response.read().strip() == 'OK':
        open(SOURCE, 'w').truncate()

    raw_input('Press Any Key to continue')

if __name__ == '__main__':
    main()
