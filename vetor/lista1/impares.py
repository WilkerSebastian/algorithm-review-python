# Faça um programa que solicite que o usuário informe valores para preencher 15 
# posições de um vetor do tipo real. 
# Em seguida, realize a impressão dos valores (conteúdo) ímpares que estão em posições
# (índices) pares presentes no vetor. 

def main():
    
    MAX_SIZE = 15
    
    valores = []
    
    i = 0
    
    print("\n")
    
    while i < MAX_SIZE:
      
      valores.append(float(input("Informe um valor: ")))
      
      i += 1
    
    print("\nEsse são os valores ímpares: ")
    for valor in list(filter(lambda x: x % 2 != 0, valores)):
        
      print(valor)
    
    return

if __name__ == "__main__":
    main()