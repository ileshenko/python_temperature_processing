from datetime import datetime
import time

class Record(object):

    def __init__(self, temperature, time):
        super(Record, self).__init__()
        self.temperature = temperature
        self.time = time

    def serialize(self):
        timestamp = int(time.mktime(self.time.timetuple()))
        return '{0}:{1}'.format(self.temperature, timestamp)
        
    def __repr__(self):
        return '<Record temp={0} time={1}>'.format(self.temperature, self.time)
