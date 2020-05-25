import os 
import base64
import json

def encode_to_json(image_file, encoding = 'base64', compression = ''):
    _, full_file_name = os.path.split(image_file)
    file_name, extention = full_file_name.split('.')

    with open( image_file, 'rb') as f:
        data = base64.b64encode(f.read()) 
    
    return json.dumps({ 'name':         file_name,
                        'format':       extention,
                        'encoding':     encoding,
                        'compression':  compression,
                        'payload':      data.decode('utf-8')})

def decode_from_json(json_data):
    json_dict = json.loads(json_data)
    if 'encoding' not in json_dict or 'payload' not in json_dict:
        return
    else:
        if json_dict['encoding'] == 'base64':
            return base64.b64decode(json_dict['payload'])
        else:
            return ""