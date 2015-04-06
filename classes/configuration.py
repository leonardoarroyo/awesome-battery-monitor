from classes import misc
import re
import os
import glob

class Configuration():
    def check(self, fatal=False):
        try:
            misc.import_from_absolute_path('/home/arroyo/.config/awesome-battery-monitor/config.py')
        except:
            if not fatal:
                print(":: Could not import configuration file.")
                self.generate()
            else:
                # If fatal, just return false and let the caller method handle it
                return False
        return True

    def generate(self):
        print(":: Generating configuration file.")
        directory = misc.config_dir()

        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except:
            pass

        f = open("{}config.py".format(directory), 'w+')
        battery_path = '/sys/class/power_supply/'

        # Default settings
        f.write("interval     = 60    # seconds\n")
        f.write("battery_path = '{}'\n\n".format(battery_path))

        # Getting batteries
        f.write("batteries = [\n".format(battery_path))
        files = glob.glob("{}BAT*".format(battery_path))

        try:
            for bat in files:
                name = re.compile(r'(BAT\d+)').findall(bat)[0]
                f.write("    '{}',\n".format(name))
        except:
            print(":: No batteries found. Exiting.")
            exit(0)

        f.write("]\n".format(battery_path))

        # Closing file
        f.close()
            

        if self.check(fatal=True):
            print(":: Config file generated.")
        else:
            print(":: Could not create {}config.py. Please check permissions.".format(directory))
            exit(0)

    def getBatteries(self):
        pass