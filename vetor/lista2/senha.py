# Faça um programa que solicite que o usuário insira 20 valores para preencher um vetor. 
# Neste cenário, cada posição de um vetor armazena um número de uma senha. Faça uma 
# funcionalidade para verificar se a senha é válida ou não. Para uma senha ser válida, 
# ela não poderá ter o mesmo número repetido por mais de 3 vezes. Por exemplo, supondo que 
# a senha seja: 01012101, note que o número 1 repetiu mais de 3 vezes. Neste caso, você 
# deverá informar ao usuário que a senha que ele digitou é inválida.
import re

def main():
    
    senha = input("informe uma senha de 20 números: ")
    
    if senha.__len__() == 20 or senhaValida(senha):
        
        print("você digitou uma senha válida!")
    else :
        
        print("você digitou uma senha inválida!")
    
    return 

def senhaValida(senha):
    
    valido = True
    
    numeros = {
        
        '0':0,
        '1':0,
        '2':0,
        '3':0,
        '4':0,
        '5':0,
        '6':0,
        '7':0,
        '8':0,
        '9':0
        
    }
    
    for x in senha:
        
        numeros[x] += 1
        
    for chave,valor in numeros.items():
        
        if valor > 3:
          
          valido = False
    
    return valido

if __name__ == "__main__":
    main()