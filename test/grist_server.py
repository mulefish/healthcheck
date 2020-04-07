from flask import Flask
from flask import render_template
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def about():
    result = {}
    result['msg'] = "This is a dummy server to mimick a bunch of endpoints"
    result['endpoints'] = ['postgres', 'mongo', 'endpoint1','endpoint2','endpoint3', 'jwttoken']
    return jsonify(result)

alphanumeric = 'abcdefghijklmnopqrstuvwxyz0123456789'

@app.route('/jwttoken')
def jwttoken(): 
    global alphanumeric
    ary = alphanumeric.split("")
    token = ""
    for i in range(50):
        token += ary[i]
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