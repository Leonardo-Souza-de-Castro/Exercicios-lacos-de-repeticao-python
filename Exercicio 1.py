valor_digitado = 0
soma = 0

while(True):
    valor_digitado = int(input("Digite um numéro: "))

    soma += valor_digitado

    if valor_digitado == 0:
        print(soma)
        break
