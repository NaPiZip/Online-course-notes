import json
import os.path


def dump_info_to_json_file(filename):
    data_dict = dict(foursquare  = dict(client_id='dummy',
                                   client_secret='dummy'),
                     mapquest    = dict(consumer_key='dummy',
                                   consumer_secret='dummy'))

    with open(filename,'w') as f:
        json.dump(data_dict,f)

def read_info_from_json_file(filename):
    with open(filename) as f:
        data = json.load(f)
    return data

def get_foursquare_key_dict():
    script_path = os.path.abspath(os.path.dirname(__file__))
    keys_dict = read_info_from_json_file(script_path+'/secrets.json')
    return keys_dict.get('foursquare')

def get_mapquest_key_dict():
    script_path = os.path.abspath(os.path.dirname(__file__))
    keys_dict = read_info_from_json_file(script_path+'/secrets.json')
    return keys_dict.get('mapquest')

if __name__=='__main__':
    debug = False
    if debug:
        filename = 'secrets.json'
        print(get_mapquest_key_dict())
        print(get_foursquare_key_dict())
