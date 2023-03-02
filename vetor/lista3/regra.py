# Faça um programa em python que verifique, para cada posição do vetor, se há algum valor cujo 
# conteúdo da posição seguinte possui 2 números a mais que ele. Por exemplo, considere 
# o vetor: 2, 3, 4, 7, 9, 8. O valor após o número 7 possui 2 números a mais que ele (9 – 7 = 2). 
# Desse modo, seu programa deverá informar que há um valor que atende a regra
import random

def main():
    
    MAX_SIZE = 10

    vetor = []
    
    i = 0
    
    while i < MAX_SIZE:
        vetor.append(random.randint(0 , 10))
        i += 1

    output = []
    
    for x in vetor:
        output.append(f"{x}")

    print("no vetor [{}]".format(",".join(output)))
    for i in range(len(vetor)-1):
        if vetor[i+1] - vetor[i] == 2:
            print(f"O valor {vetor[i]} atende à regra.")
    
    return

if __name__ == "__main__":
    main()