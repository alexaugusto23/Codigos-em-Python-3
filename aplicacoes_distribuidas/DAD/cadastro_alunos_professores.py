from flask import Flask, request, jsonify, render_template

cadastro_alunos_professores = Flask(__name__)

database = {}
database['ALUNO'] = []
database['PROFESSOR'] = []

# Rotas principais
@cadastro_alunos_professores.route('/')
def index():
    return '<h1><strong>Cadastro de Alunos e Professores</strong></h1>'

@cadastro_alunos_professores.route("/todos")
def todos():
    return jsonify(database)

@cadastro_alunos_professores.route("/reset")
def resetar():
    database['ALUNO'] = []
    database['PROFESSOR'] = []
    return jsonify(database)


# Rotas ALUNO
@cadastro_alunos_professores.route("/alunos")
def listar_alunos():
    return jsonify(database['ALUNO'])

@cadastro_alunos_professores.route("/alunos", methods = ['POST'])
def aluno_novo():
    novo_aluno = request.json
    database['ALUNO'].append(novo_aluno)
    return jsonify(database['ALUNO'])

@cadastro_alunos_professores.route('/alunos/<int:idAlu>', methods = ['GET'])
def localiza_aluno(idAlu):
    for aluno in database['ALUNO']:
        if aluno['id_aluno'] == idAlu:
            return jsonify(aluno)
        return 'não achei', 404

@cadastro_alunos_professores.route('/alunos/<int:idAlu>', methods=['DELETE'])
def apagar_aluno(idAlu):
    for aluno in database['ALUNO']: 
        if aluno['id_aluno'] == idAlu: 
            database['ALUNO'].remove(aluno)
            return jsonify(database['ALUNO'])
    return 'não achei', 404

@cadastro_alunos_professores.route('/alunos/<int:idAlu>', methods=['PUT'])
def atualizar_aluno(idAlu):
    atualiza_aluno = request.get_json()
    for aluno in database['ALUNO']: 
        if aluno['id_aluno'] == idAlu: 
            database['ALUNO'].remove(aluno)
            database['ALUNO'].append(atualiza_aluno)
            return jsonify(database['ALUNO'])
    return 'não achei', 404


# Rotas PROFESSOR
@cadastro_alunos_professores.route("/professores")
def listar_professores():
    return jsonify(database['PROFESSOR'])

@cadastro_alunos_professores.route("/professores", methods = ['POST'])
def professor_novo():
    novo_professor = request.json
    database['PROFESSOR'].append(novo_professor)
    return jsonify(database['PROFESSOR'])

@cadastro_alunos_professores.route('/professores/<int:idProfessor>', methods = ['GET'])
def localiza_professor(idProfessor):
    for professor in database['PROFESSOR']:
        if professor['id_professor'] == idProfessor:
            return jsonify(professor)
        return 'não achei', 404

@cadastro_alunos_professores.route('/professores/<int:idProfessor>', methods = ['DELETE'])
def apagar_professor(idProfessor):
    for professor in database['PROFESSOR']: 
        if professor['id_professor'] == idProfessor: 
            database['PROFESSOR'].remove(professor)
            return jsonify(database['PROFESSOR'])
    return 'não achei', 404

@cadastro_alunos_professores.route('/professores/<int:idProfessor>', methods = ['PUT'])
def atualizar_professor(idProfessor):
    atualiza_professor = request.get_json()
    for professor in database['PROFESSOR']: 
        if professor['id_professor'] == idProfessor: 
            database['PROFESSOR'].remove(professor)
            database['PROFESSOR'].append(atualiza_professor)
            return jsonify(database['PROFESSOR'])
    return 'não achei', 404


if __name__ == '__main__':
    cadastro_alunos_professores.run()