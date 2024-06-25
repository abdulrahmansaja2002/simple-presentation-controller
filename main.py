from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from helpers.key_down import left_arrow_key, right_arrow_key
from helpers.lan_ip import get_local_ip

app = Flask(__name__)
ip = get_local_ip()
port = 5000

CORS(app)


@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    return jsonify(data)

@app.route('/left', methods=['POST'])
def left():
    left_arrow_key()
    print('Left arrow key pressed and released')
    return jsonify({'message': 'Left arrow key pressed and released'})

@app.route('/right', methods=['POST'])
def right():
    right_arrow_key()
    print('Right arrow key pressed and released')
    return jsonify({'message': 'Right arrow key pressed and released'})

@app.route('/')
def index():
    return render_template('index.html', server_ip=ip, server_port=port)
if __name__ == '__main__':
    host = '0.0.0.0'
    app.run(host=host, port=port, debug=True)

