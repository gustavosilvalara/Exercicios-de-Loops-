preco_carro = int(input("Digite o preço do carro: "))
a_vista = preco_carro - (preco_carro * 0.20)
print(f"O preço final á vista com desconto de 20% é: {a_vista}")

iterador = 6
while iterador != 66:
    acrescimo = iterador / 2
    valor_parcelado = preco_carro + (preco_carro * (acrescimo / 100))
    parcelas = valor_parcelado / iterador
    print(f"O preço final parcelado em {iterador} x é de R$ {valor_parcelado:0.2f} com parcelas de "
          f"R$ {parcelas:0.2f}")
    iterador += 6