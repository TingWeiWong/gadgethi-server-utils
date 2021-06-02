import os
import re
import sys
import copy
from gadgethiServerUtils._configs import *
from gadgethiServerUtils.file_basics import *

# Autogenerate Configs
# -------------------------
default_gserver_location = os.environ.get(
    "XDG_CONFIG_HOME", os.path.expanduser(os.path.join("~", ".gserver"))
)

def generate_configs(filepath, credentials_fp="credentials.yaml"):
    """
    This is the function to generate default 
    yaml configs and default credentials configs
    * Input
        - filepath: file path to the config file. 
        - credentials_fp: file path to the credential file.
    """
    config_loc = os.path.abspath(
        os.path.join(default_gserver_location, filepath)
    )

    credentials_loc = os.path.abspath(
        os.path.join(default_gserver_location, credentials_fp)
    )
    
    # This checks the config file
    if os.path.isfile(config_loc):
        print("Config file existed.. Checking configurations meet reqs..")
        # If configs file existed in directory
        current_cfgs = read_config_yaml(config_loc)
        flag, modified_dict = GServerConfigs.check_current_configs_match_reqs(current_cfgs)

        if not flag:
            print("Requirements don't meet, adding defaults entries")
            write_yaml(config_loc, modified_dict)
    else:
        print("Config file not existed.. Generating default configuations")
        os.makedirs(os.path.dirname(config_loc), exist_ok=True)

        default_configs = copy.deepcopy(GServerConfigs.basic_configs)
        default_configs.update(GServerConfigs.aws_configs)
        write_yaml(config_loc, default_configs)

    # This checks the credential file
    if os.path.isfile(credentials_loc):
        print("Credentials file existed.. Skip Initializing..")
    else:
        os.makedirs(os.path.dirname(credentials_loc), exist_ok=True)
        write_yaml(credentials_loc, {})


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Need config file yaml path. Ex. python3 generate_configs.py config.yaml')
        sys.exit()

    # make sure the arguments meet the regex
    yaml_regex = "^.+\.yaml$"

    if not bool(re.search(yaml_regex, sys.argv[1])):
        print("Args %s is not a yaml file" % sys.argv[1])
        sys.exit(-1)

    generate_configs(sys.argv[1])