
from flask import Flask, request, jsonify
import socket
import os
from os import environ


app = Flask(__name__)

@app.route('/')
@app.route('/ip', methods=['GET'])
def name():
    
    info={}
    info["CONT_NAME"] = socket.gethostname()
    info["CONT_IP"] = socket.gethostbyname(socket.gethostname())

    if "MY_NODE_NAME" in os.environ:
    	info["MY_NODE_NAME"] = os.environ.get('MY_NODE_NAME')

    if "MY_NODE_IP" in os.environ:
    	info["MY_NODE_IP"] = os.environ.get('MY_NODE_IP')

    if "MY_POD_NAME" in os.environ:
    	info["MY_POD_NAME"] = os.environ.get('MY_POD_NAME')

    if "MY_POD_IP" in os.environ:
    	info["MY_POD_IP"] = os.environ.get('MY_POD_IP')


    #return "server_ip: " + server_ip + ",client_ip:" + client_ip +",host_name: " + host_name +",host_ip: "  + host_ip
    #return "request_host: " + request.host + ",client_ip:" + client_ip + ",container_hostname: " + host_name +",container_ip: "  + host_ip
    #return jsonify({'ip': request.remote_addr}), 200
    #return jsonify({'ip': request.environ['REMOTE_ADDR']}), 200
    return jsonify(info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)