from flask import Flask
from flask import render_template
from flask import jsonify
import random
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def about():
    result = {}
    result['msg'] = "This is a dummy server to mimick a bunch of endpoints"
    result['endpoints'] = ['postgres', 'mongo', 'endpoint1','endpoint2','endpoint3', 'jwttoken']
    return jsonify(result)

alphanumeric = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
 
@app.route('/jwttoken')
def jwttoken(): 
    global alphanumeric
    token = ""
    for i in range(50):
        token += random.choice(alphanumeric)
    return token

@app.route('/postgres')
def postgres(): 
    return "Ok"

@app.route('/mongo')
def mongo(): 
    return "Ok"

@app.route('/endpoint1')
def endpoint1(): 
    return "Ok"

@app.route('/endpoint2')
def endpoint2(): 
    return "Ok"

@app.route('/endpoint3')
def endpoint3(): 
    return "Ok"

if __name__ == '__main__':
    app.run()