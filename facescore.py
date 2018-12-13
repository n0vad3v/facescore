import requests
import json
import sys
'''
the conf file is a JSON 
{
    "api_key":"Your API Key"
    "api_secret":"Your Secret"
}
'''
'''
python facescore.py 
[-c configure_file_path] 
if dont have this ,the programming will read the default configure data
(choose 1 in 3)
[-u url]
[-f file]
[-b base64code]
'''
request_url = "https://api-cn.faceplusplus.com/facepp/v3/detect"

def read_configure_data(*args):
    #get a json configure file
    if len(args) == 0:
        conf_file = "facescore.conf"
    if len(args) == 1:
        conf_file = args[0]
    with open(conf_file) as f:
        conf_dict = json.load(f)
    return conf_dict

def post_requests(pic_path):
    


def main():
    key_list = [sys.argv[i] for i in range(len(sys.argv)) if i%2 == 0]
    value_list = [sys.argv[i] for i in range(len(sys.argv)) if i%2 == 1]
    arg_dict = {key:value for key in key_list for value in value_list}
    conf_data = read_configure_data(arg_dict.get('-c'))
    