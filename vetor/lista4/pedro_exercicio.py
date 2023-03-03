# Pedro possui muitos familiares e amigos. Nas festas de final de ano, ele gosta de realizar sorteios de
# prêmios. Os sorteios funcionam assim: o familiar ou amigo informe um número. Em seguida, Pedro
# armazena o valor e entrega um código para a pessoa. Cada familiar/amigo podem informar o número
# para o sorteio a qualquer momento. Quando Pedro sorteia um valor, ele procura, no conjunto de valores
# informados, se há algum número igual ao sorteado. Se houver, ele apresenta o(s) código(s) do(s)
# ganhador(es). Esse código é representado por um número inteiro e positivo iniciado em zero (sugiro
# que use o índice do vetor para representar o código). Faça um programa que auxilie Pedro a gerenciar
# as apostas para o sorteio. Para auxiliá-lo, implemente as opções abaixo. É importante lembrar que ele
# pode receber apenas 100 valores. Seu programa deverá executar enquanto o usuário solicitar. A cada
# execução, o usuário poderá selecionar uma das opções disponíveis.

# 1. Registro de número: Para implementar essa funcionalidade, solicite que o usuário informe um
# número e o armazene no vetor. Obs.: O usuário não precisará informar os 100 números de uma vez,
# ou seja, ele poderá informar um conjunto de números, realizar um sorteio e informar mais números.
# Após armazenar o número, apresente o código para o usuário (ou seja, realize a impressão do
# índice da posição que o número foi armazenado).

# 2. Busca premiado: Para implementar essa funcionalidade, solicite que o usuário informe o número
# que foi sorteado. Em seguida, verifique e apresente uma mensagem contendo o(s) código(s) do(s)
# ganhador(es). Considere que sempre haverá um ganhador e que os usuários poderão informar
# números repetidos. Uma pessoa é considerada como ganhadora quando o número que ela escolheu
# é igual ao número sorteado.

def main():
    
    codigos = []
    
    opcao = 0
    
    while opcao != 3:
        
        opcao = menu()
        
        if opcao == 1:
            codigos = registro(codigos)
          
        elif opcao == 2:
            busca(codigos)
    
    return

def registro(codigos):
    
    finalizou = False
    
    while not finalizou:
        
        codigos.append(int(input("\nInforme um número: ")))
        
        print(f"{len(codigos) -1}: código({codigos[len(codigos) - 1]})")
        
        finalizou = input("finlaziou (s/n): ") == "s"
    
    return codigos

def busca(codigos):
    
    codigo = int(input("\nInforme um número para ser sorteado: "))
    
    sorteados = list(filter(lambda x: x == codigo, codigos))
    
    print("\nOs sorteados foram:")
    for i , sorteado in enumerate(sorteados):
        print(f"{i}: código({sorteado})")
    
    return

def menu():
    
    opcao = 0
    
    print("\n1) Registro de número")
    print("2) Busca premiada")
    print("3) SAIR")
    opcao = int(input("escolha: "))
    
    return opcao
    

if __name__ == "__main__":
    main()