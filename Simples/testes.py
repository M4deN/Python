class node:
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

def push(self, data):

        if self.head == None:
            self.head = Node(data)

        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

def isemptystack(self,data):
    return self.data == None


def retornaelementos(self):
    if self.isempty():
        return None

    else:
        return self.head.data

def push(self, data):
