import json

def read_config_test():
    expected = ["PostGresService","MongoService","Endpoint1","Endpoint2","Endpoint3"]
    actual = []
    path = "../config.json"
    with open(path) as f:
        data = json.load(f)
        for entry in data:
            actual.append(entry['service'])
    isOk = True
    for item in expected:
        if not item in actual:
            isOk = False
    if isOk == True:
        print("PASS reading the config from {}".format(path))
    else:
        print("FAIL reading the config from {}".format(path))

def read_config_into_url_as_key_hashmap_for_endpoints():
    endpoints = {}
    path = "../config.json"
    with open(path) as f:
        data = json.load(f)
        for entry in data:
            endpoint = entry['service']
            urls = entry['urls']
            for url in urls:
                # 'endpoint' might be a dupe, but the url will not be. 
                # 'Eg' 
                # xyz.com/someservice/healthcheck 
                # vs.
                # xyz.com/someservice/mcowcount
                # Both 'healthcheck' and 'mcowcount' belong to the same service 
                endpoints[url] = endpoint 
        # for key in endpoints:
        #     val = endpoints[key]
        #     print("key {} and {} ".format( key, val ))
    isOk = len(endpoints) > 0 # Currently ought to be '5'

    if isOk == True:
        print("PASS read_config_into_url_as_key_hashmap_for_endpoints")
    else:
        print("FAIL read_config_into_url_as_key_hashmap_for_endpoints")






if __name__ == '__main__':
    read_config_test()
    read_config_into_url_as_key_hashmap_for_endpoints()
   