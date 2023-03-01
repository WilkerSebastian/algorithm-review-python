# Pedro trabalha em uma floricultura que comercializa buquês de flores. As
# flores que ele possui para fazer os buquês são: rosas cor-de-rosa escuro,
# rosas cor-de-rosa claro, rosas brancas e rosas amarelas. As flores são
# vendidas por unidade e o custo (unitário) de cada uma delas é R$ 8.00,
# R$ 7.00, R$ 9.00 e R$ 6.00, respectivamente. Considere que ele poderá
# atender apenas 10 pedidos de buquês em sua loja e que ele possui muitas
# flores em estoque. Para cada um dos pedidos, solicite o número de flores
# que o cliente deseja. Em seguida, solicite a cor de cada uma das flores. Após
# solicitar os dados do pedido, apresente o custo dele ao usuário. Realize a
# mesma tarefa para todos os pedidos. 

def main(): 
    
    quantFlores = int(input("\nInforme quantas flores deseja: "))
    
    flores = []
    
    i = 0
    
    while i < quantFlores:
        
      flor = int(input("Informe o tipo da flor (1 = rosas cor-de-rosa escuro, 2 = rosas cor-de-rosa claro, 3 = rosas brancas e 4 = rosas amarelas): "))
      
      flores.append(flowerValue(flor))
      
      i += 1
      
    outputs = []
    
    for flor in flores:
     
        outputs.append("R$ {}".format(flor))
      
    print("\nTotal a pagar: R$ {} ({})".format(sumValues(flores) , " + ".join(outputs)))
    
    return

def flowerValue(flower):
    
    valores = {
        
        1: 8,
        2: 7,
        3: 9,
        4: 6
        
    }
    
    return valores[flower]

def sumValues(valores):
    
    sum = 0
    
    for x in valores:
      sum += x
    
    return sum

if __name__ == "__main__":
    main()