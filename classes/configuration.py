from classes import misc
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

        try:            
            f = open("{}config.py".format(directory), 'w+')
            battery_path = '/sys/class/power_supply/'

            # Default settings
            f.write("interval     = 60    # seconds\n")
            f.write("battery_path = '{}'".format(battery_path))

            # Getting batteries
            files = print(glob.glob("{}BAT*".format(battery_path)))

            # Closing file
            f.close()
        except:
            pass
            

        if self.check(fatal=True):
            print(":: Config file generated.")
        else:
            print(":: Could not create {}config.py. Please check permissions.".format(directory))
            exit(0)

    def getBatteries(self):
        pass