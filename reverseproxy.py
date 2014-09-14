from flask import Flask, jsonify, make_response, request
import urllib2
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/github-webhook/", methods = ['POST'])
def handle_webhook():
    hook_json = request.json
    print hook_json

    req = urllib2.Request('http://space.sshchicago.org:49152/github-webhook')
    req.add_header('Content-Type', 'application/json')
    jenkins_response = urllib2.urlopen(req, json.dumps(hook_json))
    print response
    return jsonify({'lol': "lol"})
   
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

