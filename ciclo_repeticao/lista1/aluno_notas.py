# Considere que uma escola possui 4 alunos e cada aluno realiza uma
# quantidade específica de atividades. Faça um programa que pergunte, para
# cada estudante, quantas avaliações ele fez e qual nota de cada avaliação.
# Após receber as notas, de cada aluno, apresente a média que ele obteve. 
    
def main():
    
    alunos = 4
    i = 0

    while i < alunos:
        
        quantProvas = int(input("\nInforme a quantidade de avaliações realizou: "))
        
        notas = getNotas(quantProvas)
        
        media = calcMedia(notas)
        
        print("\nMédia: " + str(media))
        
        i+=1
        
    return 0
    
def getNotas(quantProvas):
    
    notas = []
    i = 0
    
    while i < quantProvas:
        
      nota = float(input("\nInforme sua nota: "))
        
      notas.append(nota)
      i += 1
    
    return notas
    
    
def calcMedia(notas):
    
    sumnotas = 0
    
    for nota in notas:
        sumnotas += nota
    
    return sumnotas / len(notas)

if __name__ == "__main__":
    main()