# Faça um programa que solicite que o usuário informe 10 valores. Após solicitar 
# os dados, apresente o menor valor informado. 
# Considere que todos os valores inseridos serão distintos. 

def main():
    
    MAX_VALUE = 10
    
    node = Node(MAX_VALUE)
    
    i = 0
    
    print('\n')
    
    while i < MAX_VALUE:
        
      num = int(input("Informe um valor: "))
      
      adicionar(node , num)
      
      i += 1
      
    print("\n\nMenor número informado: " + str(buscarMenor(node)))
    
    return

# Node é uma lista ligada que vou usar como arvore binaria
class Node:
    
    def __init__(self, valor):
        self.esquerda = None
        self.direita = None
        self.valor = valor

def adicionar(node, valor):
    
    if node is None:
        return Node(valor)
    else:
        if node.valor < valor:
            node.direita = adicionar(node.direita, valor)
        else:
            node.esquerda = adicionar(node.esquerda, valor)
    return node

def buscarMenor(node):
    if node is None:
        return None
    elif node.esquerda is None:
        return node.valor
    else:
        return buscarMenor(node.esquerda)

if __name__ == "__main__":
    main()