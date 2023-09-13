valor_digitado = int(input("Digite o número desejado: "))
existe = 0


for i in range(1,(valor_digitado + 1)):
    if valor_digitado % i == 0:
        existe += 1
    else:
        existe += 0

if existe == 2:
    print("Número primo")
else:
    print("Número não primo")