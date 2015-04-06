import datetime
import time

class Battery():
    def getCapacity():
        f = open(CAPACITY, 'r')
        capacity = f.read().strip()
        f.close()
        return capacity

        

    def getStatus():
        f = open(STATUS, 'r')
        status = f.read().strip()
        f.close()
        return status



    def getStatusLine():
        date = datetime.datetime.now()
        status_line = "{}% {} {}".format(self.getCapacity(), self.getStatus(), date)
        return status_line