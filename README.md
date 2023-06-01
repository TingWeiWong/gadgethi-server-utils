# gadgethiServerUtils
This is the utility helper functions that can support the gadgethi server development. 

## New in 0.3.0
* GadgethiServer.py
	1. Remove test keyword argument. Testing uses another structure so this parameter is not needed anymore. 
	2. *NEED IMMEDIATE ACTION* table_list now only accept full name and does not assume "\_table" suffix.
	3. *NEED IMMEDIATE ACTION* credential_path now needs to be provided to the server instance. 
* authentication.py
	1. *NEED IMMEDIATE ACTION* Class Renamed to GadgethiHMAC256Verification, GadgethiHMAC256Encryption. Doday Util client needs to refer to the new clients. (However, we recommend to use GadgethiClient instead of DodayHttpClient)
* GadgethiClient.py
	1. *NEED IMMEDIATE ACTION* For future HTTP client. Refer to the spec of this new file. 


## New in 0.3.38
* GadgethiServer.py
	* include Threading in the server
	* include do_OPTIONS
	* include headers flexibility
	* include CORS options
		default to True be
		send_header('Access-Control-Allow-Origin', '*')
		send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
		send_header("Access-Control-Allow-Headers", 
'DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range,Gadgethi-Key,Hmac256-Result,time,Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers')
