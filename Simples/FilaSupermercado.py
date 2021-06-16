pessoas = []
temp = []
clientes = []
valor = input().split(" ")
valor2 = [int(valor[0]), int(valor[1])]
valor = input().split(" ")
contador = 0
while True:
    try:
        pessoas.append(int(valor[contador]))
        temp.append(0)
        contador = contador + 1
    except IndexError:
        contador = 0
        break
valor = input().split(" ")
while True:
    try:
        clientes.append(int(valor[contador]))
        contador = contador + 1
    except IndexError:
        contador = 0
        break
while True:
    try:
        temp[contador] = pessoas[contador] * clientes[0]
        clientes.pop(0)
        contador = contador + 1
    except IndexError:
        break
while 0 < len(clientes):
    fim = temp.index(min(temp))
    temp[fim] = temp[fim] + pessoas[fim] * clientes[0]
    clientes.pop(0)
print(max(temp))

