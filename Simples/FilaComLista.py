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

if __name__ == '__main__':

    Fila = FilaListaEncadeada()
    Fila.Enfileirar(10)
    Fila.Enfileirar(20)
    Fila.Enfileirar(30)
    Fila.Desenfileirar()
    Fila.Enfileirar(40)
    Fila.Enfileirar(50)
    Fila.Enfileirar(60)
    Fila.Desenfileirar()
    Fila.Enfileirar(70)

    Fila.imprimir()

    print("\nPrimeiro Elemento " + str(Fila.front.dados))

    print("\nUltimo Elemento " + str(Fila.rear.dados))

    print("\ndesenfileirando o primeiro elemento")
    Fila.Desenfileirar()

    Fila.imprimir()
