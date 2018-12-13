import requests
import json
import sys
'''
python facescore.py 
[-c configure_file_path] 
if dont have this ,the programming will read the default configure file
the configure file is a JSON 
{
    "api_key":"Your API Key"
    "api_secret":"Your Secret"
}
(choose 1 in 3)
[-u url]
[-f file]
[-b base64code]
use like 'python facescore.py -c facescore.conf -f mypic.jpg'
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

def get_response_data(conf_data):
    try:
        r = requests.post(request_url,data = conf_data,content = 'form-data')
        r.raise_for_status()
        return r.text
    except:
        print('requests error')

def parse_data(json_data):
    pass

def main():
    requests_type = ""
    key_list = [sys.argv[i] for i in range(len(sys.argv)) if i%2 == 0]
    value_list = [sys.argv[i] for i in range(len(sys.argv)) if i%2 == 1]
    arg_dict = {key:value for key in key_list for value in value_list}
    conf_data = read_configure_data(arg_dict.get('-c'))
    if conf_data is None:
        print('WTF the arguments you write')
        return 
    if conf_data.get('-u') is not None:
        conf_data['image_url'] = conf_data.get('-u')
        requests_type = 'image_url'
    elif conf_data.get('-f') is not None:
        conf_data['image_file'] = conf_data.get('-f')
        requests_type = 'image_file'
    elif conf_data.get('-b') is not None:
        conf_data['image_base64'] = conf_data.get('-b')
        requests_type = 'image_base64'
    else :
        print('WTF the arguments you write')
        return 

if __name__ == "__main__":
    main()