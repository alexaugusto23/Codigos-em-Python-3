from flask import Flask, render_template, request
appform = Flask(__name__)

@appform.route("/")
def ola_mundo():
    return render_template("indexform.html"), 200

@appform.route("/tipoget")
def ir_get():
    return render_template("get.html"), 200

@appform.route("/tipopost")
def ir_post():
    return render_template("post.html"), 200

@appform.route("/receber/", methods=['GET','POST'])
def receber():
    if request.method == "GET":
        return "GET!<br>Nome: {} <br>Idade: {}".format(request.args.get("nome"),request.args.get("idade")), 200
    elif request.method == "POST":
        return "POST!<br>Nome: {} <br>Idade: {}".format(request.form["nome"],request.form["idade"]), 200

if __name__ == '__main__':
    appform.run(debug=True)