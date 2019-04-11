import json


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


if __name__=='__main__':
    filename = 'secrets.json'
    dump_info_to_json_file(filename)
    print(read_info_from_json_file(filename))
