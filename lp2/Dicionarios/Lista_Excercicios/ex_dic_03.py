# Se quiser testar sem digitar o input:

kart = {'A': [10.0, 10.0, 12.0, 15.0],   #47
        'B': [10.0, 9.0, 10.0, 19.0],    #48
        'C': [9.0, 9.0, 11.0, 11.0],     #40
        'D': [10.0, 10.0, 15.0, 8.0],    #43
        'E': [13.0, 13.0, 14.0, 15.0]}   #55

'''
# Usuário cadastra corredor e valor da volta
for cadastro_nome in range(5):
    nome = input("Nome: ")
    kart[nome] = []
    for corrida_volta in range(4):
        volta = float(input("Tempo de volta:"))
        kart[nome].append(volta)
'''
# Quem ganhou a corrida
t_min = 8000
for piloto in kart:
    temp = sum(kart[piloto])
    if temp < t_min:
        t_min = temp
        nome = piloto
        
print("Ganhou a corrida:", nome, t_min)

# Volta mais rápida
v_min_global = 500
for piloto in kart:
    v_min_piloto = 500
    for volta in kart[piloto]:
        temp = volta
        if temp < v_min_piloto:
            v_min_piloto = temp
    if v_min_piloto < v_min_global:
        v_min_global = v_min_piloto
        nome = piloto
print("Volta mais rapida:", nome, v_min_global)
