
from flask import Flask, request, jsonify
import socket


app = Flask(__name__)

@app.route('/ip', methods=['GET'])
def name():
    client_ip=request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    server_ip=request.host.split(':')[0]
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)

    #return "server_ip: " + server_ip + ",client_ip:" + client_ip +",host_name: " + host_name +",host_ip: "  + host_ip
    return "request_host: " + request.host + ",client_ip:" + client_ip + ",container_hostname: " + host_name +",container_ip: "  + host_ip
    #return jsonify({'ip': request.remote_addr}), 200
    #return jsonify({'ip': request.environ['REMOTE_ADDR']}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)