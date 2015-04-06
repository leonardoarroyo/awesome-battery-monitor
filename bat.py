#!/bin/env python
from classes import configuration, misc
import time
    
if __name__ == "__main__":
    config = configuration.Configuration()
    config.check()

    batteries = config.getBatteries()
    while(True):
	    for battery in batteries:
	    	status = battery.getStatusLine()
	    	config.saveStatusLine(status)
	    time.sleep(config.getInterval())