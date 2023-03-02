# Faça um programa que solicite que o usuário informe valores para preencher dois vetores com 5
# posições. Seu programa deverá realizar e exibir a multiplicação do conteúdo da primeira posição 
# do primeiro vetor com a última posição de outro vetor. Em seguida apresente a multiplicação 
# da segunda posição do primeiro vetor com a penúltima posição do segundo vetor e assim 
# sucessivamente. Será necessário apresentar apenas a multiplicação dos dados.

# Exemplo considerando 2 vetores com 3 posições:
# Primeiro vetor: 2, 4, 6
# Segundo vetor: 3, 7, 6
# Resultado: 12, 28, 18

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
      
    print("\n")
    for x in range(MAX_SIZE):
      
      valor1 = vetor1[x]
      
      valor2 = vetor2[(len(vetor2) - 1) - x]
      
      print(f"{valor1 * valor2} ({valor1} * {valor2})")
    
    return

if __name__ == "__main__":
    main()