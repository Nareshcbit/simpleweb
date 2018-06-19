
from flask import Flask, request, jsonify
import socket
import os


app = Flask(__name__)

@app.route('/')
@app.route('/ip', methods=['GET'])
def name():
    
    info={}
    info["client_ip"] = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    info["server_ip"] = request.host.split(':')[0]
    info["cont_name"] = socket.gethostname()
    info["cont_ip"] = socket.gethostbyname(socket.gethostname())

    info["md_node_name"] = os.environ.get('MD_NODE_NAME') or 'NA'
    info["md_node_ip"] = os.environ.get('MD_NODE_IP') or 'NA'
    info["md_pod_name"] = os.environ.get('MD_POD_NAME') or 'NA'
    info["md_pod_ip"] = os.environ.get('MD_POD_IP') or 'NA'

    #return "server_ip: " + server_ip + ",client_ip:" + client_ip +",host_name: " + host_name +",host_ip: "  + host_ip
    #return "request_host: " + request.host + ",client_ip:" + client_ip + ",container_hostname: " + host_name +",container_ip: "  + host_ip
    #return jsonify({'ip': request.remote_addr}), 200
    #return jsonify({'ip': request.environ['REMOTE_ADDR']}), 200
    return jsonify(info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)