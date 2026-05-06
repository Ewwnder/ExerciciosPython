C = int(input())

for _ in range(C):
    conta = input()
    partes_conta = conta.split()

    valor1 = int(partes_conta[0])
    operador = partes_conta[1]
    valor2 = int(partes_conta[2])
    resposta = int(partes_conta[4])

    if operador == '+':
        correta = valor1+valor2
    elif operador == '-':
        correta = valor1-valor2
    else:
        correta = valor1*valor2

    tentativa = abs(correta-resposta)-1


    print("Er"+"r"*tentativa+"ou!")
