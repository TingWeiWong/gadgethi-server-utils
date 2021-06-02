import unittest
import threading
from gadgethiServerUtils.GadgethiServer import *

class GServerTests(unittest.TestCase):
    """
    Testing Strategy

    - constructor:
        partition on table_list: length 0, >0
        partition on initialized_func_list: length 0, >0
        partition on desc: string length 0, >0
        partition on yaml_exccondition returns: all True, all False, some True some False
        partition on configs: empty dictionary, keys > 0
        partition on service_handler: Normal return true, normal return false, exception
        partition on config_path: file exists, file not exists
        partition on credential_path: file exists, file not exists
        partition on custom_event_handler: Normal return true, normal return false, exception
        partition on fetch_yaml_from_s3: True, False
        partition on authentication: True, False

    - handling:
        partition on HTTP types: GET, POST, OPTIONS, PUT
        partition on authentication: with auth header, without auth header
        partition on event handler type: custom event handler, gadgethi service handler
        partition on POST application types: json, urlencode, raw
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

    # def test_00(self):
    #   self.assertTrue(self.start_server_instance())
