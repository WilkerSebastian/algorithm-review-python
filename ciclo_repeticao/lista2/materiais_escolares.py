# Paula deseja comprar materiais escolares para seus filhos. Ela possui 2 filhos que chamam: Luiz 
# e Robson. Cada um dos filhos precisa comprar um conjunto específico de materiais, 
# sendo eles: caderno, caneta, borracha e lápis. Considere que: (I) os materiais custam 
# R$ 13.00, R$ 3.00, R$ 2.00 e R$ 1.50, respectivamente; (II) o usuário informará um produto 
# por vez; (III) o usuário poderá repetir o produto quantas vezes desejar. Por exemplo, ele
# poderá informar que deseja comprar uma caneta, um caderno e outra caneta. Seu programa deverá 
# solicitar o nome (ou código) de cada produto que deseja comprar e encerrar a solicitação de dados
# quanto o usuário desejar. Considere que cada filho fará as compras de uma vez, ou seja, primeiro 
# Luiz fará suas compras e depois será a vez de Robson. Ao encerrar a compra, de cada um dos 
# filhos, apresente o total gasto por eles. 

def main():
    
    custoTotal = 0
    
    encerrou = True
    
    while encerrou:
        
        produto = int(input("\nInforme o produto que deseja: (1 = caderno; 2 = caneta; 3 = borracha; 4 = lápis): "))
    
        custoTotal += materialCost(produto)
    
        encerrou = int(input("Encerrou seu pedido? (1 = sim e 2 = não): ")) != 1
        
    print("\nTotal a pagar: R$ {}".format(custoTotal))
    
    return 0

def materialCost(produto): 
    
    custos = {
        
        1: 13,
        2: 3, 
        3: 2,
        4: 1.5
        
    }
    
    return custos[produto]

if __name__ == "__main__":
    main()