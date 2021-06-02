import requests
from gadgethiServerUtils.authentication import *
from gadgethiServerUtils.time_basics import timeout

"""
Represents the client class to send
HTTP requests. Including gadgethi
authentication function. 
"""
class GadgetHiClient:
    """
    TODO:
        extend functionalities of adding
        external headers. 
    """
    def __init__(self, **configs):
        """
        @kwargs: if _http_url in kwargs, 
            get that key and set it to the
            attribute. 
        """
        for key in configs:
            if "_http_url" in key:
                setattr(self, key, configs[key])

    def __getitem__(self, key):
        return getattr(self, key)
    
    @timeout(5)
    def client_get(self, key, input_dict, gauth=False, **configs):
        """
        This is the main function to send out HTTP GET. 
        @params key: the key of the url stored in the ADT
        @params input_dict: the input dictionary of the data that is 
            going to send
        @params gauth: whether we should enable gadgethi authentication, 
            adding auth headers to the HTTP packets
        """
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
        """
        This is the main function to send out HTTP POST. 
        @params key: the key of the url stored in the ADT
        @params input_dict: the input dictionary of the data that is 
            going to send
        @params gauth: whether we should enable gadgethi authentication, 
            adding auth headers to the HTTP packets
        @params urlencode: This defines the application type of the POST content. 
            If True -> www-urlencode, default False -> json
        """
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