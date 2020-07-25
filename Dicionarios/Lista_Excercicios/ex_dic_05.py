inventario = {'ouro': 500,
              'bolsa': ['pedra', 'fio', 'pepita'],
              'mochila': ['gaita', 'adaga', 'saco de dormir', 'pão']}

inventario['bolso'] = None
inventario['bolso'] = ['concha','fruta','moeda']
inventario['mochila'].sort()
inventario['mochila'].remove('adaga')
inventario['ouro'] = [500,50,330]
inventario['ouro'][0] += 50
inventario['ouro'][1] += 50
inventario['ouro'][2] += 70

print(inventario)