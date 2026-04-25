colaboradores = int(input("Informe o número de colaboradores: "))
iterador = 0
segunda = 0
terca = 0
quarta = 0
quinta = 0
sexta = 0
dia_escolhido = ""

while iterador != colaboradores:
    dia_semana = input("Informe o dia da sua preferência (segunda-feira, terça-feira,"
                       " quarta-feira, quinta-feira sexta-feira: ")
    if dia_semana == "segunda-feira" or dia_semana == "segunda":
        segunda += 1
    elif (dia_semana == "terca-feira" or dia_semana == "terça-feira" or dia_semana == "terca"
          or dia_semana ==  "terça"):
        terca += 1
    elif dia_semana == "quarta-feira" or dia_semana == "quarta":
        quarta += 1
    elif dia_semana == "quinta-feira" or dia_semana == "quinta":
        quinta += 1
    else:
        sexta += 1
    iterador += 1

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    dia_escolhido = "segunda-feira"
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    dia_escolhido = "terca-feira"
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    dia_escolhido = "quarta-feira"
elif quinta > segunda and quinta > terca and quinta > quarta and quinta> sexta:
    dia_escolhido = "quinta-feira"
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    dia_escolhido = "sexta-feira"
else:
    if segunda == terca and segunda != 0 and terca != 0:
        dia_escolhido = "empate entre segunda-feira e terça-feira"
    elif segunda == quarta and segunda != 0 and quarta != 0:
        dia_escolhido = "empate entre segunda-feira e quarta-feira"
    elif segunda == quinta and segunda != 0 and quinta != 0:
        dia_escolhido = "empate entre segunda-feira e quinta-feira"
    elif segunda == sexta and segunda != 0 and sexta != 0:
        dia_escolhido = "empate entre segunda-feira e sexta-feira"
    elif terca == quarta and terca != 0 and quarta != 0:
        dia_escolhido = "empate entre terca-feira e quarta-feira"
    elif terca == quinta and terca != 0 and quinta != 0:
        dia_escolhido = "empate entre terca-feira e quinta-feira"
    elif terca == sexta and terca != 0 and sexta != 0:
        dia_escolhido = "empate entre terca-feira e sexta-feira"
    elif quarta == quinta and quarta != 0 and quinta != 0:
        dia_escolhido = "empate entre quarta-feira e quinta-feira"
    elif quarta == sexta and quarta != 0 and sexta != 0:
        dia_escolhido = "empate entre quarta-feira e sexta-feira"
    elif quinta == sexta and quinta != 0 and sexta != 0:
        dia_escolhido = "empate entre quinta-feira e sexta-feira"

print(f"O dia escolhido pelos colaboradores é: {dia_escolhido}")