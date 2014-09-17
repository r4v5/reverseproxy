from flask import Flask, jsonify, make_response, request
import urllib2
import json

jenkins_url = "http://mlearn.sshchicago.org:8080"


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/github-webhook/", methods = ['POST'])
def handle_webhook():
    hook_json = request.json
    print hook_json
    crumb_request = urllib2.Request(jenkins_url + "/crumbIssuer/api/json")
    crumb_response = urllib2.urlopen(crumb_request)
    csrf_crumb = json.loads(crumb_response.read())
    print "Crumb received: " + csrf_crumb['crumbRequestField'] + csrf_crumb['crumb']
    proxied_request = urllib2.Request(jenkins_url + '/github-webhook/')
    proxied_request.add_header('Content-Type', 'application/json')
#    proxied_request.add_header(csrf_crumb['crumbRequestField'], csrf_crumb['crumb'])
    jenkins_response = urllib2.urlopen(proxied_request, json.dumps(hook_json))
    print jenkins_response
    return jenkins_response.json

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)




