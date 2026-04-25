while True:
    print("""Escolha o tipo de investimento:
1. CDB
2. LCI
3. LCA
0. Sair
    """)
    escolha = int(input("Digite o tipo de investimento ou saida (0, 1, 2 ou 3): "))
    if escolha != 1 and escolha != 2 and escolha != 3 and escolha != 0:
        print("Escolha uma opção valida!!")
        continue
    elif escolha == 0:
        print("Finalizando o programa...")
        break
    else:
        if escolha == 1:
            porcentagem_ir = 0
            valor_resgatado = int(input("Digite o valor a ser resgatado: "))
            numero_de_dias = int(input("Digite o número de dias que o valor permaneceu"
                                   " investido: "))
            if numero_de_dias <= 180:
                porcentagem_ir = 22.5 / 100
            elif numero_de_dias <= 360:
                porcentagem_ir = 20 / 100
            elif numero_de_dias <= 720:
                porcentagem_ir = 17.5 / 100
            elif numero_de_dias > 720:
                porcentagem_ir = 15 /100
            valor_ir = valor_resgatado * porcentagem_ir
            print(f"O valor do imposto de renda a ser pago é: {valor_ir}\n")
        elif escolha == 2:
            valor_resgatado = int(input("Digite o valor a ser resgatado: "))
            numero_de_dias = int(input("Digite o número de dias que o valor permaneceu"
                                       " investido: "))
            print(f"O valor do imposto de renda a ser pago é: R$0,00\n")
        else:
            valor_resgatado = int(input("Digite o valor a ser resgatado: "))
            numero_de_dias = int(input("Digite o número de dias que o valor permaneceu"
                                       " investido: "))
            print(f"O valor do imposto de renda a ser pago é: R$0,00\n")