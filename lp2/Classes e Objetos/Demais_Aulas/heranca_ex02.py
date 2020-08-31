class Funcionario:
    def __init__(self, nome, endereco, telefone, cpf, numero_cpts, salario):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.cpf = cpf
        self.numero_cpts = numero_cpts
        self.salario = salario


class Tecnicos_Administrativos(Funcionario):
    def __init__(self, nome, endereco, telefone, cpf, numero_cpts, salario, cargo):
        super().__init__(nome, endereco, telefone, cpf, numero_cpts, salario)
        self.cargo = cargo


class Professor(Funcionario):
    def __init__(self, nome, endereco, telefone, cpf, numero_cpts, salario, titulacao, area_pesquisa):
        super().__init__(nome, endereco, telefone, cpf, numero_cpts, salario)
        self.titulacao = titulacao
        self.area_pesquisa = area_pesquisa
        self.disciplinas = []


class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.disciplinas = []


class Disciplina:
    def __init__(self, nome, codigo_diciplina, carga_hor, curso):
        self.nome = nome
        self.codigo_diciplina = codigo_diciplina
        self.carga_hor = carga_hor
        self.curso = curso

class Curso:
    def __init__(self, nome, codigo_curso, duracao):
        self.nome = nome
        self.codigo_curso = codigo_curso
        self.duracao = duracao

curso = Curso("ADS", 1111, 3)
disciplina1 = Disciplina("PL1", 1, 40, curso)
disciplina2 = Disciplina("Banco de Dados", 2, 80, curso)

prof = Professor("Caio", "Rua A", 999999999, 12345678912, 1235, 5000, "Matematico", "Linguagem")
prof.disciplinas.append(disciplina1)
prof.disciplinas.append(disciplina2)

for item in prof.disciplinas:
    print(item.nome)

aluno = Aluno("André")
aluno.disciplinas.append(disciplina1)
print(aluno.disciplinas[0].carga_hor)


