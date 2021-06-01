import requests
from gadgethiServerUtils.authentication import *
from gadgethiServerUtils.time_basics import timeout


class GadgetHiClient:
	"""
	This is the http client
	class. 
	"""
	def __init__(self, **configs):
		for key in configs:
			if "_http_url" in key:
				setattr(self, key, configs[key])

	def __getitem__(self, key):
		return getattr(self, key)
	
	@timeout(5)
	def client_get(self, key, input_dict, gauth=False, **configs):
		
		get_query = self[key]

		# assign query list
		query_list = ["?"]
		for key in input_dict:
			query_list.extend([str(key), "=", input_dict[key], "&"])

		# concatenate together
		get_query += "".join(query_list[:-1])

		if gauth:
			# authentication
			a = GadgethiHMAC256Encryption(configs['gadgethi_key'],configs['gadgethi_secret'])
			headers = a.getGServerAuthHeaders()
			r = requests.get(get_query,headers=headers)
		else:
			r = requests.get(get_query)
		response = r.text 
		return response

	@timeout(5)
	def client_post(self, key, input_dict,gauth=False,urlencode=False, **configs):

		post_query = self[key]

		if gauth:
			# authentication
			a = GadgethiHMAC256Encryption(configs['gadgethi_key'],configs['gadgethi_secret'])
			headers = a.getGServerAuthHeaders()

			if urlencode:
				r = requests.post(post_query, data=input_dict,headers=headers)
			else:
				r = requests.post(post_query, json=input_dict,headers=headers)
			response = r.text			
		else:

			if urlencode:
				r = requests.post(post_query, data=input_dict)
			else:
				r = requests.post(post_query, json=input_dict)
			response = r.text

		return response