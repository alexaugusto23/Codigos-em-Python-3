from flask import Flask, request, jsonify, render_template

# Criação da instância
app = Flask(__name__)

# Rota 1
@app.route("/")
def index():
    return (render_template("index.html")),200

# Rota 2
@app.route("/usuario")
@app.route("/usuario/<name>")
def user(name=None):
    return render_template("index.html", name = name),200

if __name__ == '__main__':
    app.run(debug=True)