from flask import Flask, jsonify
from hack_backend import get_sports
from flask_cors import CORS
 
app = Flask(name)
CORS(app)
user_input = input()
@app.route("/")
def hello_world():

    return jsonify(get_sports(keyword= user_input))

if __name__ == "__main__":
    app.run(host='localhost', port=9874)
