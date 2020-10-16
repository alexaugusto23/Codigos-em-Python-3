from flask import Flask, request, jsonify

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

@app.route("/todos")
def todos():
    return jsonify(database)

@app.route("/alunos")
def listar_alunos():
    return jsonify(database['ALUNO'])

@app.route("/alunos", methods = ['POST'])
def aluno_novo():
    novo_aluno = request.json
    database['ALUNO'].append(novo_aluno)
    return jsonify(database['ALUNO'])

@app.route("/alunos/<int:id_aluno>", methods = ['GET'])
def localiza_aluno(id_aluno):
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            return jsonify(aluno)
        return 'não achei', 404


@app.route("/professores")
def listar_professores():
    return jsonify(database['PROFESSOR'])

@app.route("/professores", methods = ['POST'])
def professor_novo():
    novo_aluno = request.json
    database['PROFESSOR'].append(novo_aluno)
    return jsonify(database['PROFESSOR'])

@app.route("/alunos/<int:id_professor>", methods = ['GET'])
def localiza_aluno(id_professor):
    for professor in database['PROFESSOR']:
        if professor['id'] == id_professor:
            return jsonify(professor)
        return 'não achei', 404

if __name__ == '__main__':
    app.run()