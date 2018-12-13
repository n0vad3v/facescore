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


def read_configure_data(conf_file_path):
    #get a json configure file
    if conf_file_path is None:
        conf_file = "facescore.conf"
    else :
        conf_file = conf_file_path
    # print(conf_file)
    with open(conf_file) as f:
        conf_dict = json.load(f)
    return conf_dict

def get_response_data(conf_data,*args):
    try:
        r = requests.post(request_url,data = conf_data)
        r.raise_for_status()
        print(r.text)
        return r.text
    except:
        print('requests error')

def parse_data(json_data):
    pass

def main():
    requests_type = ""
    key_list = [sys.argv[i] for i in range(1,len(sys.argv)) if i%2 == 1]
    value_list = [sys.argv[i] for i in range(1,len(sys.argv)) if i%2 == 0]
    arg_dict = {key:value for key in key_list for value in value_list}
    conf_data = read_configure_data(arg_dict.get('-c'))
    if conf_data is None:
        print('WTF the -c arguments you write')
        return 
    #这里赋值有问题
    if arg_dict.get('-u') is not None:
        conf_data['image_url'] = arg_dict['-u']
        requests_type = 'image_url'
    elif arg_dict.get('-f') is not None:
        conf_data['image_file'] = open(arg_dict['-f'],'rb')
        requests_type = 'image_file'
    elif arg_dict.get('-b') is not None:
        conf_data['image_base64'] = arg_dict['-b']
        requests_type = 'image_base64'
    if requests_type == "":
        print('WTF the -u|-f|-b arguments you write')
        return
    json_data = get_response_data(conf_data)

if __name__ == "__main__":
    main()