
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ip', methods=['GET'])
def name():
    client_ip=request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    server_ip=request.host.split(':')[0]
    return server_ip + " : " + client_ip
    #return jsonify({'ip': request.remote_addr}), 200
    #return jsonify({'ip': request.environ['REMOTE_ADDR']}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)