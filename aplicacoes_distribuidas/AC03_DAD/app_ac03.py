from flask import Flask, request, jsonify, render_template
import requests

app_ac03 = Flask(__name__)

@app_ac03.route("/")
@app_ac03.route("/index")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    applogin.run(debug=True)