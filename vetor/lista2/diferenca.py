# Faça um programa que solicite que o usuário preencha um vetor do tipo real com 10 posições. 
# Após a inserção dos dados, verifique e informe qual é a diferença entre o conteúdo de cada 
# posição com o conteúdo da posição posterior a ele. Exemplo: se os números 2, 5, 1 estiverem 
# contidos no vetor, a resposta considerando apenas estes números será: -3 (2 - 5) e 4 (5 - 1), 
# respectivamente.

def main():
    
    MAX_SIZE = 10
    
    valores = []
    
    i = 0
    
    print("\n")
    
    while i < MAX_SIZE:
      
      valores.append(int(input("Informe um valor: ")))
      
      i += 1
      
    i = 0
    while i < MAX_SIZE:
        
      print("{} ({} - {})".format(valores[i] - valores[i + 1], valores[i], valores[i + 1]))
      
      i += 2
    
    return

if __name__ == "__main__":
    main()