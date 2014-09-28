from flask import Flask, jsonify, make_response, request
import requests
import urllib2
import urllib
import json
import pdb

jenkins_url = "http://mlearn.sshchicago.org:8080"
needs_crumb = False

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/github-webhook/", methods = ['POST'])
def handle_webhook():
    hook = request.form['payload']
    print hook
    if needs_crumb:
        crumb_request = requests.get(jenkins_url + "/crumbIssuer/api/json")
        csrf_crumb = crumb_request.json()
        print "Crumb received: " + csrf_crumb['crumbRequestField'] + csrf_crumb['crumb']
    data = [('payload', hook)]
    jenkins_response = requests.post(jenkins_url + "/github-webhook/", data=data )
    print jenkins_response.status_code
    return jenkins_response.text

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
