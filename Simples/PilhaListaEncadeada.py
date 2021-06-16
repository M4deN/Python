class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class PilhaListaEncadeada:

    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    def empilhar(self, data):

        if self.head == None:
            self.head = Node(data)

        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def exclui(self):

        if self.isempty():
            return None

        else:

            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

    def desempilha(self):

        if self.isempty():
            return None

        else:

            list = self.head
            self.head = self.head.next
            list.next = None
            return list.data

    def inicio(self):

        if self.isempty():
            return None

        else:
            return self.head.data

    def imprimir(self):

        iternode = self.head

        if self.isempty():

            print("Pilha Está Vazia ")

        else:

            while (iternode != None):

                print(iternode.data, "->", end = " ")

                iternode = iternode.next

            return


Pilha = PilhaListaEncadeada()

Pilha.empilhar(1)
Pilha.empilhar(2)
Pilha.empilhar(3)
Pilha.empilhar(4)
Pilha.empilhar(5)
Pilha.empilhar(6)
Pilha.empilhar(7)
Pilha.imprimir()

print("\nPrimeiro Elemento:", Pilha.inicio())

Pilha.exclui()

Pilha.imprimir()

print("\nRemovendo o primeiro elemento da pilha....")

print("\nAgora o Primeiro Elemento é:", Pilha.inicio())

print("\nDesempilhando o elemento:",Pilha.desempilha())

print("\nA Pilha agora é composta por")

Pilha.imprimir()


