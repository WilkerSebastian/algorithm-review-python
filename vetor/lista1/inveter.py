# Faça um programa que solicite que o usuário informe valores para preencher 10 posições de um vetor
# do tipo inteiro. Em seguida, realize a impressão dos valores informados de trás para frente, ou seja,
# apresente o último valor inserido, em seguida, o penúltimo valor e assim por diante. 

def main():
    
    MAX_SIZE = 10
    
    valores = []
    
    i = 0
    
    print("\n")
    
    while i < MAX_SIZE:
      
      valores.append(int(input("Informe um valor: ")))
      
      i += 1
    
    print("\nEsse são os valores de tras pra frente: ")
    
    i = len(valores) -1
    while i > -1:
        
      print(valores[i])
      
      i -= 1
    
    return

if __name__ == "__main__":
    main()