lista = []

while True:
    try:
        num = int(input("Digite um valor: "))
    except ValueError:
        print("Digite somente valores inteiros para formar sua lista.")
        continue

    if num in lista:
        print ("esse número já existe e está duplicado, portanto, não foi adicionado")
    elif num not in lista:
        lista.append(num)
        print ("Valor adicionado com sucesso")

    continuar = input("Quer continuar? S/N: ")
    if continuar.upper() == "S":
        continue
    elif continuar.upper()== "N":
        break
print (f"Você criou a lista: {sorted(lista)}")