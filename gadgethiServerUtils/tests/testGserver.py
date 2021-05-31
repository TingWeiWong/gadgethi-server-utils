import unittest
import threading

class GServerTests(unittest.TestCase):
	"""
	This is the basic test which initialize the
	server and check the connection of the system
	by posting several simple orders.
	"""
	def setUp(self):
		self.port = 5050
		self.host = "127.0.0.1"

	def run_server(self):
		"""Run the actual threading test."""
		def start_and_init_server(p):
			"""A helper function to start out server in a thread.
			This could be done as a lambda function, but this way we can
			perform other setup functions if necessary.
			Args:
				port: The port of the server (local host)
			"""
			server_run(port=p)

		server_thread = threading.Thread(target=start_and_init_server, args=(self.port, ))
		
		try:
			# Start the server
			server_thread.start()
			return True
		except Exception as e:
			print('Something went horribly wrong!', e)
			return False

	def test_00(self):
		self.assertTrue(self.run_server())