from flask import Flask, render_template, request
import requests

applogin = Flask(__name__)

usuarios = [
    {'login': 'aluno1', 'senha': 'azul'},
    {'login': 'aluno2', 'senha': 'vermelho'}
    ]

dados = {}

@applogin.route("/login", methods=["GET"])
def login():
    return render_template("login.html", mensagem = "Entre no sistema"),200

@applogin.route("/cadastro", methods=["GET"])
def cadastro():
    return render_template("cadastro.html", mensagem = "Preencha o seu Cadastro"),200

@applogin.route("/form_teste", methods=["PUT", "POST"])
def form_teste():
    login = request.form["login"]
    senha = request.form["password"]
    for user in usuarios:
        if user['login'] == login and user['senha'] == senha:
            return render_template("login_ok.html", login = login)
    return render_template("login.html", mensagem = "Login inválido.")

@applogin.route("/form_cadastro", methods=["POST"])
def form_cadastro():
        nome = request.form["nome"]
        cpf = request.form["cpf"]
        email = request.form["email"]
        telefone = request.form["telefone"] 
        cep = request.form["cep"]
        return render_template("form_cadastro.html")

def procura_cep(cep):
    resposta = requests.get('https://viacep.com.br/ws/'+cep+'/json/')
    print (f'\nURL:{resposta.url}\nStatus:{resposta.status_code}\nRequest:{resposta.request}\n')   
    dic = resposta.json()
    return dic

if __name__ == '__main__':
    applogin.run(debug=True)