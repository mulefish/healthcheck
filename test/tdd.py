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


if __name__ == '__main__':
    read_config_test()