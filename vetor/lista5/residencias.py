# Ana possui 100 residências dispostas uma ao lado da outra. Ela aluga as casas e precisa de
# sua ajuda para administrar o aluguel. Cada casa possui um número inteiro, sequencial e
# positivo iniciado em zero que a identifica 
# (dica: use um vetor para representar as casas e o índice do vetor para identificá-las). 
# Faça um programa que contenha 4 funcionalidades, descritas abaixo. 
# Seu programa deverá executar enquanto o usuário solicitar. 
# A cada iteração, ele poderá solicitar a opção que deseja executar.

# 1. Aluguel de casa: para essa funcionalidade, o usuário informará o número de uma casa e
# seu programa deverá verificar se ela está livre. Se estiver, reserve-a.

# 2. Liberação de casa: para essa funcionalidade, o usuário informará o número de uma casa
# e seu programa deverá verificar se ela está ocupada. Se estiver, libere-a.

# 3. Valor a receber: considere que o aluguel de cada casa é R$500,00. Quando o usuário
# selecionar essa opção, verifique quantas casas estão ocupadas e calcule o valor que ele
# deverá receber com o aluguel de todas elas.

# 4. Busca de casa livre: quando o usuário selecionar essa opção, apresente o número (índice)
# de cada uma das casas que estão livres no condomínio.

def main():
    
    casas = []
    
    opcao = 0
    
    for i in range(100):
        casas.append("livre")
    
    while opcao != 5:
        
        opcao = menu()
        
        if opcao == 1:
            casas = aluguel(casas)
          
        elif opcao == 2:
            casas = liberacao(casas)
             
        elif opcao == 3:
            receber(casas)
            
        elif opcao == 4:
            buscar(casas)
            
def aluguel(casas):
    
    index = int(input("\nInforme o número da casa que quer alugar: "))

    if casas[index] == "livre":
        casas[index] = "ocupada"
    
    return casas

def liberacao(casas):
    
    index = int(input("\nInforme o número da casa que quer liberar: "))

    if casas[index] == "ocupada":
        casas[index] = "livre"
    
    return casas

def receber(casas):
    
    ocupadas = list(filter(lambda x: x == "ocupada", casas))
    
    lucro = len(ocupadas) * 500 # 500 é custo da casa aluguel da casa
    
    print(f"\nvocê recebera R$ {lucro}.00, de {len(ocupadas)} casas alugadas")
    
    return
    
def buscar(casas):
    
    print("\ncasas livres: \n")
    for i, casa in enumerate(casas):
        if casa == "livre":
            print(f"({i}): {casa}")
    
    return
            
def menu():
    
    opcao = 0
    
    print("\n1) Aluguel de casa")
    print("2) Liberação de casa")
    print("3) Valor a receber")
    print("4) Busca de casa livre")
    print("5) Sair")
    
    opcao = int(input("escolha: "))
    
    return opcao

if __name__ == "__main__":
    main()