import os
import sys
from gadgethiServerUtils.file_basics import *

def generate_configs():
	"""
	This is the function to generate default 
	yaml configs
	"""
config_loc = os.path.abspath(
        os.path.join(default_config_location, "catsoop", "config.py")
    )
    if os.path.isfile(config_loc):
    	pass


if __name__ == '__main__':
	generate_configs()