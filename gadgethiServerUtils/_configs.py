import copy
import os
import re
import sys
from file_basics import *

"""
Holds the required configs
for several use cases. 
"""
class GServerConfigs:
    """
    Immutable configs object that stores
    all the default config keys and values
    of basic use case. 
    """
    basic_configs = {
        # The info of the main server
        "server_address": "127.0.0.1",
        "server_port": "5050",

        "log_file_path": "/opt/doday/LOG_FILES/",
        "log_file_header": "gadgethi-default-server-",

        "server_api_path": "yamls/server_api.yaml",
        "allowed_ip": ["*"]
    }

    doday_configs = {
        # The info of the websocket server which the main server connects
        "websocket_ip": "127.0.0.1",
        "websocket_port": 9001,
        "websocket_mode": "client",
        # Business Hour
        "opening_time": "10:00",
        "closing_time": "23:50",

        "database_name": "gadgethi-database-001",
        "order_invoice_bucket": "doday-order-invoice",
        "order_invoice_url_header": "https://doday-order-invoice.s3-ap-southeast-1.amazonaws.com/",
        
        # Special hours
        "special_hours":
        [{
            "type": "by-days",
            "arg": [7, [1, 3]], # [days (monday =1, sunday = 7), index of that day of the month, 
            # e.g. 1st and 3rd monday]
            "hours": {
              "opening_time": "11:30",
              "closing_time": "21:00"
            }
          },
          # just an example, not doing anything now. 
          # by dates have higher priority so need to be later in the list
          {
            "type": "by-dates",
            "arg": [16, 17, 18, 19, 20], # [1st of that month]
            "hours": {
              "opening_time": "XX", # write "XX" if not in business that day
              "closing_time": "XX"
            }
          }],
    }

    aws_configs = {
        "yaml_s3_bucket": "gadgethi-bucket001",
        "yaml_s3_folder": "doday_yamls/",
        "yaml_local_folder": "yamls/",
        "s3_database_ini_path": "database_ini/database.ini",
        "local_database_ini_path": "/Users/weitung/.gserver/database.ini"
    }

    def __init__(self, doday_flag=False, aws_flag=True):
        """
        @params doday_flag: attach doday related server configs
        @params aws_flag: attach aws yaml fetch related configs
        """
        configs = {}
        configs.update(self.basic_configs)

        if doday_flag:
            configs.update(self.doday_configs)

        if aws_flag:
            configs.update(self.aws_configs)

        # Use super class to set attributes to bypass
        # the immutable properties. 
        for key in configs.keys():
            super(GServerConfigs, self).__setattr__(key, configs[key])

    def __setattr__(self, key, value):
        """Prevent modification of attributes."""
        raise AttributeError('GServerConfigs cannot be modified')

    @classmethod
    def check_current_configs_match_reqs(cls, current_cfgs):
        """
        This is the class method function to check
        whether the input configs matches minimal requirement
        -> at least the basic requirements
        @returns status, newly_produced_dict_that_matches_req:
        status indicates current_cfgs matches or not. 
        """
        input_defensive_copy = copy.deepcopy(current_cfgs)
        if set(cls.basic_configs.keys()).issubset(set(current_cfgs.keys())):
            return True, input_defensive_copy

        new_return_dict = copy.deepcopy(cls.basic_configs)
        new_return_dict.update(input_defensive_copy)
        return False, new_return_dict


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
        - filepath: 
    """
    config_loc = os.path.abspath(
        os.path.join(default_gserver_location, filepath)
    )

    credentials_loc = os.path.abspath(
        os.path.join(default_gserver_location, credentials_fp)
    )

    print(config_loc)
    print(credentials_loc)
    if os.path.isfile(config_loc):
        print("Config file existed.. Checking configurations meet reqs..")
        # If configs file existed in directory
        current_cfgs = read_config_yaml(config_loc)
        flag, modified_dict = GServerConfigs.check_current_configs_match_reqs(current_cfgs)

        if not flag:
            print("Requirements don't meet, adding defaults entries")
            write_yaml(config_loc, modified_dict)

    if os.path.isfile(credentials_loc):
        print("Credentials file existed.. Initializing a blank file. ")

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
