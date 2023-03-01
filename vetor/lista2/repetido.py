# Faça um programa que solicite que o usuário insira 10 valores para preencher um vetor. 
# Em seguida, verifique e informe se há números repetidos no vetor ou não.

def main():
    
    MAX_SIZE = 10
    
    valores = []
    
    i = 0
    
    print("\n")
    
    while i < MAX_SIZE:
      
      valores.append(int(input("Informe um valor: ")))
      
      i += 1
      
    print("\nvalores repetidos:")
    for valorRepetido in search(valores, True):
      print(valorRepetido)
    
    print("\nvalores não repetidos: ")
    for valorNaoRepetido in search(valores, False):
      print(valorNaoRepetido)
    
    return

def search(array, repetido):
    
    newArray = []
    tabela_hash = {}
    
    for elemento in array:
        if elemento in tabela_hash:
            tabela_hash[elemento] += 1
        else:
            tabela_hash[elemento] = 1

    for chave, valor in tabela_hash.items():
        if valor > 1 and repetido:
            newArray.append(chave)
        elif valor == 1 and not repetido:
            newArray.append(chave)

    return newArray

if __name__ == "__main__":
    main()