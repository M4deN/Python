class Node:
    def __init__(self, dados):
        self.dados = dados
        self.next = None

class FilaListaEncadeada:

    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    def Enfileirar(self, item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def Desenfileirar(self):

        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next

        if (self.front == None):
            self.rear = None

    def imprimir(self):

        iternode = self.front

        if self.isEmpty():

            print("Fila Está Vazia ")

        else:

            while (iternode != None):

                print(iternode.dados, "->", end = " ")

                iternode = iternode.next

            return
Fila = FilaListaEncadeada()
a, b = input().split()
Fila.Enfileirar(a)
Fila.Enfileirar(b)
c = (input())
for i in a:
    d = (input())
    print("entrou aqui",d)

for i in c:
    f = (input())
    print("entrou aqui", f)

while i < c:

        if i < a:

            temp = b * a

        else:
            valor2 = temp
            z = 0
        for i in a:
            if valor2 > temp:
                valor2 = temp
                z = i
                temp += b * a
                z = 0

for i in a:
	if valor2 < temp:
		valor2 = temp
		print("valor e\n", valor2)

Fila.imprimir()