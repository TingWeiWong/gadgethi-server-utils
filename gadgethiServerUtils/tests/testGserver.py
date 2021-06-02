import unittest
import threading
from gadgethiServerUtils.file_basics import *
from gadgethiServerUtils.GadgethiServer import *
from gadgethiServerUtils.GadgethiClient import *

class GServerTests(unittest.TestCase):
    """
    Testing Strategy
    
    @ GServer
    - constructor:
        partition on table_list: length 0, >0
        partition on initialized_func_list: length 0, >0
        partition on desc: string length 0, >0
        partition on yaml_exccondition returns: all True, all False, some True some False
        partition on configs: empty dictionary, keys > 0
        partition on service_handler: Normal return true, normal return false, exception
        partition on config_path: file exists, file not exists
        partition on credential_path: file exists, file not exists
        partition on custom_event_handler: None, Normal return true, normal return false, exception
        partition on fetch_yaml_from_s3: True, False
        partition on authentication: True, False

    - handling:
        partition on HTTP types: GET, POST, OPTIONS, PUT
        partition on authentication: with auth header, without auth header
        partition on event handler type: custom event handler, gadgethi service handler
        partition on POST application types: json, urlencode, raw

    @GClient
    - constructor:
        partition on input kwargs: with '_http_url' string, without http_url string    

    - client_get:
        partition on key: key exists, key not exists
        partition on input_dict: empty, keys > 0, input_dict key type not string
        partition on timeout status: timeout, not timeout
        partition on gauth: True, False

    - client_post:
        partition on key: key exists, key not exists
        partition on input_dict: empty, keys > 0, input_dict key type not string
        partition on timeout status: timeout, not timeout
        partition on gauth: True, False
        partition on urlencode: True, False

    """

    def start_server_instance(self, **kwargs):
        """Run the actual threading test."""
        def start_and_init_server(kwargs):
            """A helper function to start out server in a thread.
            This could be done as a lambda function, but this way we can
            perform other setup functions if necessary.
            Args:
                kwargs: all necessary kwargs for gadgethi server
            """
            GadgetHiServer(**kwargs).run()

        server_thread = threading.Thread(target=start_and_init_server, args=(kwargs, ))
        
        try:
            # Start the server
            server_thread.start()
            return True
        except Exception as e:
            print('Something went horribly wrong!', e)
            return False

    def test_00(self):
      self.assertTrue(self.start_server_instance(table_list = [],
        initialize_func_list=[], 
        desc="", 
        yaml_exccondition=lambda **kwargs: True, 
        configs={}, 
        service_handler=lambda: {"indicator":True, "message": "test success"}, 
        config_path=os.path.abspath(os.path.join(default_gserver_location, "config", "config.yaml")),
        credential_path=os.path.abspath(os.path.join(default_gserver_location, "credentials.yaml")),
        authentication=False,
        custom_event_handler=None, # gadgethi handler scheme
        fetch_yaml_from_s3=False))

    def test_01(self):
      # self.assertTrue(self.start_server_instance(table_list = ["order_table", "promotion_table"],
      #   initialize_func_list=[lambda: None], 
      #   desc="GadgetHi Main", 
      #   yaml_exccondition=lambda: False, 
      #   configs={"dblock": 100}, 
      #   service_handler=lambda: {"indicator":False, "message": "test failed"}, 
      #   config_path=os.path.abspath(os.path.join(default_gserver_location, "config", "config.yaml")),
      #   credential_path=os.path.abspath(os.path.join(default_gserver_location, "credentials.yaml")),
      #   authentication=True,
      #   custom_event_handler=None,
      #   fetch_yaml_from_s3=False))
        pass