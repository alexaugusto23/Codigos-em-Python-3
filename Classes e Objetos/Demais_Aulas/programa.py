import empresa
#from empresa import Funcionario
lista_func = []

f = empresa.Funcionario("Paulo", 9614)
lista_func.append(f)

f = empresa.Funcionario("Julio", 7624)
lista_func.append(f)

f = empresa.Funcionario("Henrique", 1234)
lista_func.append(f)

f = empresa.Funcionario("Sandro", 4321)
lista_func.append(f)

sal = 1000
for func in lista_func:
    func.set_salario(sal)
    print(func.get_matricula(),func.get_nome(),func.get_salario())
    sal += 200

print("\n")

for func in lista_func:
    print(func.get_matricula(),func.get_nome(),func.get_salario())
