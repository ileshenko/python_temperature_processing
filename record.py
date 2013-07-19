from datetime import datetime
import time

class Record(object):

    def __init__(self, temperature, time):
        super(Record, self).__init__()
        self.temperature = temperature
        self.time = time

    def serialize(self):
        timestamp = int(time.mktime(self.time.timetuple()))
        return '{0} {1}'.format(timestamp, self.temperature)

    def __lt__(self, other):
        return self.time < other.time

    def __eq__(self, other):
        return self.time == other.time
        
    def __repr__(self):
        return '<Record temp={0} time={1}>'.format(self.temperature, self.time)
