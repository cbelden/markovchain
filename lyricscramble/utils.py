import json


def RetreiveRequestInfo():
    # read in config file and return json data
    json_fp = open('settings/config.json', 'r')
    data = json.load(json_fp)
    json_fp.close()

    return data
