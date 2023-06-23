from flask import Flask
import base64

app = Flask(__name__)

@app.route("/")
def print_b64_name():
    name ="Sebastian Bustamante"
    encoded = base64.b64encode(name)
    return encoded

if __name__ == '__main__':
    app.run(host='localhost', port=80)