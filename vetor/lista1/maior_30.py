# Faça um programa que solicite que o usuário informe valores para preencher 10 posições de um vetor
# do tipo real. Em seguida, realize a impressão de todos os valores maiores que 30 que estão 
# presentes no vetor

def main():
    
    MAX_SIZE = 10
    
    valores = []
    
    i = 0
    
    print("\n")
    
    while i < MAX_SIZE:
      
      valores.append(float(input("Informe um valor: ")))
      
      i += 1
    
    print("\nEsse são os valores maiores que 30: ")
    for valor in list(filter(lambda x: x > 30, valores)):
        
      print(valor)
    
    return

if __name__ == "__main__":
    main()