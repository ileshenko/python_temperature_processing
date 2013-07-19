from datetime import datetime

class Record(object):

    def __init__(self, temperature, time):
        super(Record, self).__init__()
        self.temperature = temperature
        self.time = time
        
    def __repr__(self):
        return '<Record temp={0} time={1}>'.format(self.temperature, self.time)
