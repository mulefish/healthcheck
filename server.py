from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
import json
import requests
import random
app = Flask(__name__, static_url_path='')

trampolineEndpoints = {}

@app.route('/')
def index():
    print("this is index  ")
    return app.send_static_file('index.html')

@app.route('/getTrampolineEndpoints')
def getTrampolineEndpoints():
    return jsonify(trampolineEndpoints)



@app.route('/trampoline_test', methods=['POST'])
def trampoline_test():
    # This test needs test/grist_server.py to be running! 
    content = request.json
    url = "http://localhost:5000/endpoint3"
    headers = {
    }
    response = requests.request("GET", url, headers=headers)
    result = response.text
    return jsonify({"result":result})

if __name__ == '__main__':
        
    trampolineEndpoints = {}
    path2 = "config.json"
    with open(path2) as f:
        trampolineEndpoints = json.load(f)

    app.run(host='0.0.0.0', port=8080)