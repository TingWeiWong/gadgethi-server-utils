#-*-coding:utf-8 -*-
import threading

# from helper.order_helper import *
# from helper.data_helper import *
# from helper.menu_helper import *
# import helper.tableinit_helper as inittable

from gadgethiServerUtils.exceptions import *
from gadgethiServerUtils.db_operations import *
from gadgethiServerUtils.time_basics import *
from gadgethiServerUtils.GadgethiServer import GadgetHiServer, GadgetHiHTTPHandler
from gadgethiServerUtils.file_basics import load_config

import datetime
import json
import sys
from os.path import expanduser

# -----------------------
# Former safe get and safe post
# def safe_keys_handle(request, api_context, reqtype="GET", timezone=8, **contextArgs):
# 	'''
# 	Make sure that the format of the get 
# 	request aligns with the server. 
# 	Otherwise give clear execption details
# 	- Input:
# 		* Actual HTTP request
# 		* api_context from the api yaml
# 	'''	
# 	if reqtype == "GET":
# 		prefix_key = "values"
# 	elif reqtype == "POST":
# 		prefix_key = "form"
# 	else:
# 		raise GadosServerError("Didn't specify a request type")

# 	if prefix_key not in request:
# 		raise GadosServerError( "Fail to process with empty content")

# 	get_request_dict = {}
# 	operation = extract_arguments(request,prefix_key,['operation'])
# 	get_request_dict["operation"] = operation

# 	for mandatory_key in api_context[operation]["Mandatory"]:
# 		get_request_dict[mandatory_key] = extract_arguments(request,prefix_key,[mandatory_key])

# 	# Check YAML Validity
# 	assert len(api_context[operation]["Optionals"]) == len(api_context[operation]["OptionalDefaults"])
	
# 	for kidx in range(len(api_context[operation]["Optionals"])):
# 		optional_key = api_context[operation]["Optionals"][kidx]
# 		optional_default = api_context[operation]["OptionalDefaults"][kidx]
# 		# handle special optional key
# 		if "*SPECIAL-OPTIONAL*" in str(optional_default):
# 			key_name = optional_default.replace('*SPECIAL-OPTIONAL*', '')

# 			# Try to find operation specific optionals before using key general optionals
# 			try:
# 				optional_default = eval(key_name+"_specialoptional_"+operation)(timezone)
# 			except:
# 				optional_default = eval(key_name+"_specialoptional")(timezone)

# 		get_request_dict[optional_key] = extract_optionals(request,prefix_key,[optional_key], optional_default)

# 	if "SpecialKey" in api_context[operation]:
# 		# Need special handling -> e.g. Intella Payment Data
# 		for special_key in api_context[operation]["SpecialKey"]:
# 			# Try to find operation specific special key before using key general special key
# 			try:
# 				get_request_dict[special_key] = eval(special_key+"_specialkey_"+operation)(request, **contextArgs)
# 			except:
# 				get_request_dict[special_key] = eval(special_key+"_specialkey")(request, **contextArgs)
			
# 	return get_request_dict

# def handle_services(request, api_context, reqtype, **server_configs):
# 	"""
# 	This is the GET handler function for order service
# 	- Currently it supports (in abstract level):
# 		1. GET queue (next queue, all queue)
# 		2. GET machine info (available, preparing, locked)
# 		3. GET admin (DELETE, RESTART ALL, ADD)
# 	"""
# 	if reqtype == "GET":
# 		prefix_key = "values"
# 	elif reqtype == "POST":
# 		prefix_key = "form"
# 	else:
# 		raise GadosServerError("Didn't specify a request type")

# 	operation = extract_arguments(request,prefix_key,['operation'])
# 	get_data = safe_keys_handle(request, api_context[reqtype], reqtype=reqtype, **server_configs)

# 	try:
# 		operation_handler = eval(operation+"_handler")
# 	except:
# 		raise GadosServerError("This server doesn't handle the operation: "+str(operation))

# 	if "Arguments" in api_context[reqtype][operation]:
# 		# Update operation specific arguments
# 		server_configs.update(api_context[reqtype][operation]["Arguments"])

# 	return operation_handler(get_data, **server_configs)

# # Helper functiona
# # -----------------------
# def get_values_from_key_with_specific_pattern(iterable, pattern):
# 	"""
# 	This is the helper function for getting values from key 
# 	with specific pattern.
# 	"""
# 	out = []
# 	for key in iterable:
# 		if pattern in key:
# 			out.append(iterable[key])
# 	return out

def main_handler(event, **configs):
	"""
	"""
	pass

def pull_yaml_exception(**kwargs):
	"""
	Return true if we don't want pull this
	yaml down. False if we let it go . 
	"""
	obj_name = kwargs["obj_name"]
	if len(obj_name) < 3:
		return True #not a yaml
	if "availability" in obj_name and is_time_between(datetime.time(3,30), datetime.time(14,00)):
		return True


if __name__ == "__main__":
	# doctest.testmod()   #This enable the doctest

	# Check test mode
	if len(sys.argv) == 2:
		test=sys.argv[1]=="test"
	else:
		test = False

	# Pass in all init table functions
	# initialize_func_list = get_values_from_key_with_specific_pattern(inittable.__globals, '_initialize_')

	server = GadgetHiServer(test=test, 
		table_list = ["order", "promotion", "menu", "cart"],
		initialize_func_list=[], 
		desc="GadgetHi Main", 
		yaml_exccondition=pull_yaml_exception, 
		configs={}, 
		service_handler=lambda: None, 
		http_handler_cls=GadgetHiHTTPHandler, 
		config_path=expanduser("~")+"/.gserver/config/config-onlineserver.yaml",
		custom_event_handler=main_handler)

	server.run()