# Faça um programa que solicite que o usuário informe valores para preencher 10 posições 
# de um vetor do tipo inteiro. Em seguida, apresente os valores inseridos em par, ou seja, 
# apresente os conteúdos dos índices 0 e 1; 2 e 3; 4 e 5; 6 e 7. 
# O mesmo raciocínio deve ser seguido para os demais índices. 

def main():
    
    MAX_SIZE = 10
    
    valores = []
    
    i = 0
    
    print("\n")
    
    while i < MAX_SIZE:
      
      valores.append(float(input("Informe um valor: ")))
      
      i += 1
    
    print("\nEsse são os valores em duplas: ")
    i = 0
    while i < MAX_SIZE:
        
      print("{} e {}".format(valores[i], valores[i + 1]))
      
      i += 2
    
    return

if __name__ == "__main__":
    main()