from flask import Flask
import base64

app = Flask(__name__)

@app.route("/")
def print_b64_name():
    encoded = base64.b64encode(b'Sebastian Bustamante')
    return encoded

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)