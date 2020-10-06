class Pilha:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            raise Exception('Pilha vazia')
        return self.items.pop()
    def top(self):
        if self.is_empty():
            raise Exception('Pilha vazia')
        return self.items[-1]
    # M ́etodo "especial" que permite utilizarmos a fun ̧c~ao len() pr ́e-definida na linguagem Python
    # em uma inst^ancia da classe Pilha.
    def __len__(self):
        return len(self.items)

pilha = Pilha()
pilha.push(1)
pilha.push(2)
pilha.push(3)
pilha.push(4)
print('Pilha vazia?', pilha.is_empty())
print('Topo:', pilha.top())
print(pilha.pop())
print(pilha.pop())
print(pilha.pop())
print(pilha.pop())
print('Pilha vazia?', pilha.is_empty())

pilha2 = Pilha()
pilha2.push('a')
pilha2.push('b')
print('Topo da pilha:', pilha2.top()) # Topo da pilha: 'b'
pilha2.push('c')
print('Topo da pilha:', pilha2.top()) # Topo da pilha: 'c'
pilha2.pop() # Remove 'c'
print('Topo da pilha:', pilha2.top()) # Topo da pilha: 'b'
print('Tamanho da pilha:', len(pilha2)) # opera ̧c~ao que usa o m ́etodo especial __len__()
print('Pilha vazia?', pilha2.is_empty())
pilha2.push('d')
pilha2.pop() # Remove 'd'
pilha2.pop() # Remove 'b'
print('Topo da pilha:', pilha2.top()) # Topo da pilha: 'a'