total_dias = int (input())

idade_ano=total_dias/365
total_dias=total_dias%365
idade_meses=total_dias/30
total_dias=total_dias%30
idade_dias=total_dias

print(int(idade_ano),' ano (s)')
print(int(idade_meses),'mes (es)')
print(idade_dias, 'dia (s)')
