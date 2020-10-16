from flask import Flask

app = Flask(__name__)

database = {}
database['ALUNO'] = []
database['PROFESSOR'] = []

@app.route("/")
def index():
    return "<h1>Carregando a minha primeira Página Flask</h1>"

@app.route("/teste")
def teste():
    return "<h1>Teste - Página Flask</h1>"

@app.route("/user/<name>")
def user(name):
    return "<h1>Hello, {}!</h1>".format(name)



if __name__ == '__main__':
    app.run()