import unittest
import threading
from gadgethiServerUtils.GadgethiServer import *

class GServerTests(unittest.TestCase):
	"""
	This is the basic test which initialize the
	server and check the connection of the system
	by posting several simple orders.
	"""
	def setUp(self):
		self.port = 5050
		self.host = "127.0.0.1"

	def start_server_instance(self, **kwargs):
		"""Run the actual threading test."""
		def start_and_init_server(kwargs):
			"""A helper function to start out server in a thread.
			This could be done as a lambda function, but this way we can
			perform other setup functions if necessary.
			Args:
				port: The port of the server (local host)
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
	# 	self.assertTrue(self.start_server_instance())
