# Faça um programa que solicite que o usuário informe valores para preencher 5 posições de um vetor
# do tipo inteiro. Após solicitar os dados, realize o produtório dos valores múltiplos de 4. 
# A multiplicação deverá ser feita entre os números. 
# Por exemplo, sendo os números 4, 8 e 12, o resultado será 4*8*12=384.

def main():
    
    MAX_SIZE = 5
    
    valores = []
    
    multiResult = 1
    
    multiplos = []
    
    i = 0
    
    print("\n")
    
    while i < MAX_SIZE:
      
      valores.append(int(input("Informe um valor: ")))
      
      i += 1
    
    multiplos = list(filter(lambda x: x % 4 == 0, valores))
      
    for x in multiplos:
      multiResult *= x
    
    multiplos = list(map(lambda x: str(x), multiplos))
      
    print("\nResultado: {} = {}".format("*".join(multiplos), multiResult))
    
    return

if __name__ == "__main__":
    main()