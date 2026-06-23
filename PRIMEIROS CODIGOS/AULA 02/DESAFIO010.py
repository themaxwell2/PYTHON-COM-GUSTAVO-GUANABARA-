print("===== COMPRE DOLARES =====")

dinheiro = float(input("Digite quanto voce tem: "))
dolar = 3.27
print("Valor do dolar: {}".format(dolar))

compra = int(input("Quantos dolares voce quer comprar?:"))

quantidade = compra * dolar
comprou = quantidade - dinheiro
quantidadeDolar = dinheiro - quantidade

print("Voce comprou {} dolares!\nSeu dinheiro: {}\nSeus dolares: {} ".format(compra, comprou, quantidadeDolar ))



