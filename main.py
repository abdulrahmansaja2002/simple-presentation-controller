from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from helpers.key_down import left_arrow_key, right_arrow_key
from helpers.lan_ip import get_local_ip

# taken from: https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask#answer-42791810
# serve static files from the root directory
app = Flask(__name__,
            static_url_path='', 
            static_folder='web/static',
            template_folder='web/templates')

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
    return render_template('index.html')
if __name__ == '__main__':
    host = '0.0.0.0'
    app.run(host=host, port=port, debug=True)

