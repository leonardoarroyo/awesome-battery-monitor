import datetime
import time

class Battery():
    def __init__(self, name, battery_path="/"):
        self.name = name
        self.file = "{}{}".format(battery_path, name)

    def getCapacity(self):
        f = open("{}/capacity".format(self.file), 'r')
        capacity = f.read().strip()
        f.close()
        return capacity

    def getStatus(self):
        f = open("{}/status".format(self.file), 'r')
        status = f.read().strip()
        f.close()
        return status

    def getStatusLine(self):
        date = datetime.datetime.now()
        status_line = "{}% {} {} #{}\n".format(self.getCapacity(), self.getStatus(), date, self.name)
        return status_line