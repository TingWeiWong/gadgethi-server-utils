import unittest
import os
import shutil
from gadgethiServerUtils._configs import *
from gadgethiServerUtils.file_basics import *
from gadgethiServerUtils.scripts import generate_configs

class ScriptsTests(unittest.TestCase):
    """
    Testing Strategy:
    - generate_configs
        - partition on config file existence: config file exist, config file not exist
        - partition on credential file existence: credential file exist, credential file not exist
    """
    default_gserver_location = os.environ.get(
        "XDG_CONFIG_HOME", os.path.expanduser(os.path.join("~", ".gserver"))
    )
    # covers generate_configs cases
    def test_generate_configs_file(self):

        # Generate config file
        directory = "config_test"
        file = "config.yaml"
        credentials = "credentials.yaml"
        fp = "/".join([directory, file])
        cp = "/".join([directory, credentials])

        generate_configs.generate_configs(fp, cp)
        config_loc = os.path.abspath(
            os.path.join(self.default_gserver_location, fp)
        )
        credentials_loc = os.path.abspath(
            os.path.join(self.default_gserver_location, cp)
        )
        self.assertTrue(os.path.isfile(config_loc))
        self.assertTrue(os.path.isfile(credentials_loc))

        config_dict = read_config_yaml(config_loc)
        self.assertTrue(set(GServerConfigs.basic_configs.keys()).issubset(set(config_dict.keys())))
        self.assertTrue(set(GServerConfigs.aws_configs.keys()).issubset(set(config_dict.keys())))

        # Exist case
        generate_configs.generate_configs(fp, cp)

        self.assertTrue(os.path.isfile(config_loc))
        self.assertTrue(os.path.isfile(credentials_loc))

        config_dict = read_config_yaml(config_loc)
        self.assertTrue(set(GServerConfigs.basic_configs.keys()).issubset(set(config_dict.keys())))
        self.assertTrue(set(GServerConfigs.aws_configs.keys()).issubset(set(config_dict.keys())))

        # remove config file
        shutil.rmtree(os.path.abspath(os.path.join(self.default_gserver_location, directory)))

        # Check no residuals
        self.assertFalse(os.path.isfile(config_loc))
        self.assertFalse(os.path.isfile(credentials_loc))

