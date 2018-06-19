
from flask import Flask, request, jsonify
import socket
import os
from os import environ


app = Flask(__name__)

@app.route('/')
@app.route('/ip', methods=['GET'])
def name():
    
    info={}
    info["CLIENT_IP"] = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    info["CONT_NAME"] = socket.gethostname()
    info["CONT_IP"] = socket.gethostbyname(socket.gethostname())

    if "MD_NODE_NAME" in os.environ:
    	info["MD_NODE_NAME"] = os.environ.get('MD_NODE_NAME')

    if "MD_NODE_IP" in os.environ:
    	info["MD_NODE_IP"] = os.environ.get('MD_NODE_IP')

    if "MD_POD_NAME" in os.environ:
    	info["MD_POD_NAME"] = os.environ.get('MD_POD_NAME')

    if "MD_POD_IP" in os.environ:
    	info["MD_POD_IP"] = os.environ.get('MD_POD_IP')


    #return "server_ip: " + server_ip + ",client_ip:" + client_ip +",host_name: " + host_name +",host_ip: "  + host_ip
    #return "request_host: " + request.host + ",client_ip:" + client_ip + ",container_hostname: " + host_name +",container_ip: "  + host_ip
    #return jsonify({'ip': request.remote_addr}), 200
    #return jsonify({'ip': request.environ['REMOTE_ADDR']}), 200
    return jsonify(info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)