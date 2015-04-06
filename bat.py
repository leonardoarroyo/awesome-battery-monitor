#!/bin/env python
from classes import battery, configuration

## Config
CAPACITY = '/sys/class/power_supply/BAT0/capacity'
STATUS   = '/sys/class/power_supply/BAT0/status'

    
if __name__ == "__main__":
    config = configuration.Configuration()
    config.check()