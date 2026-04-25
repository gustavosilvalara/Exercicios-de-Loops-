valor_divida = int(input("Digite o valor da dívida: "))

print(f"Total:R$ {valor_divida:0.2f} Juros:R$ 0,00 Número de parcelas: 1 Valor da Parcela:"
      f"R$ {valor_divida}")

iterador = 3
porcentagem_juros = 10
while iterador != 15:
    juros = valor_divida * (porcentagem_juros / 100)
    divida_com_juros = valor_divida + juros
    parcelas = divida_com_juros / iterador

    print(f"Total:R$ {divida_com_juros:0.2f} Juros:R$ {juros:0.2f} Número de parcelas:"
          f" {iterador} Valor da Parcela:R$ {parcelas:0.2f}")

    porcentagem_juros += 5
    iterador += 3
