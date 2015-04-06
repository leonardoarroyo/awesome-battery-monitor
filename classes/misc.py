import os

def import_from_absolute_path(fullpath, global_name=None):
    """Dynamic script import using full path."""
    import os
    import sys

    script_dir, filename = os.path.split(fullpath)
    script, ext = os.path.splitext(filename)

    sys.path.insert(0, script_dir)
    try:
        module = __import__(script)
        if global_name is None:
            global_name = script
        globals()[global_name] = module
        sys.modules[global_name] = module
    finally:
        del sys.path[0]


def config_dir():
    return os.path.expanduser("~/.config/awesome-battery-monitor/")