# Faça um programa que solicite que o usuário insira valores para preencher 2 vetores de 10 posições
# cada. Em seguida, realize e informe a multiplicação de cada elemento do primeiro vetor com todos 
# os elementos do segundo vetor, ou seja, primeiro apresente o resultado da multiplicação do conteúdo 
# da primeira posição do primeiro vetor com o conteúdo de todas as posições do segundo vetor. 
# Em seguida, realize a multiplicação do conteúdo da segunda posição do primeiro vetor com o conteúdo 
# de todas as posições do segundo vetor e assim sucessivamente. 

def main():
    
    MAX_SIZE = 10
  
    vetor1 = []
    vetor2 = []
    
    print("Valores do primeiro vetor")
    for x in range(MAX_SIZE):
      vetor1.append(int(input("Informe um valor: ")))
      
    print("\nValores do segundo vetor")
    for x in range(MAX_SIZE):
      vetor2.append(int(input("Informe um valor: ")))
      
    for x in range(MAX_SIZE):
      
      valor1 = vetor1[x]
      
      print(f"\nvalores refentes {valor1} * x:")
      for y in range(MAX_SIZE):
        
        valor2 = vetor2[(len(vetor2) - 1) - y]
        
        print(f"{valor1 * valor2} ({valor1} * {valor2})")
    
    return

if __name__ == "__main__":
    main()