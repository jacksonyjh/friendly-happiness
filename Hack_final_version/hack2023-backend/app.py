from flask import Flask, jsonify
from hack_backend import get_sports
from flask_cors import CORS
 
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    
    return jsonify(get_sports(keyword="basketball"))
    