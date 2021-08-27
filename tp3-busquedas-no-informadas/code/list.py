class LinkedList:
    class Node:
        def __init__(self, value, key = None):
            self.value = value;
            self.key = key;
            self.next = None;
            self.prev = None;
    def __init__(self):
        self.head = None;
        self.tail = None;
        self.length = 0;
    
    def push (self, value, key = None):
        self.enqueue(value, key);
    
    def priorityPush(self, value, key = None):
        newNode = self.Node(value, key);
        self.length += 1;
        node = self.head
        #Si tiene elementos
        if(node):
            #Si tiene que insertarse en la cabecera
            if (node.value >= value):
                self.push(value);
            else:
                while (node.next):
                    if(node.next.value >= value):
                        #Conecta con el nodo de adelante
                        node.next.prev = newNode;
                        newNode.next = node.next;
                        #Conecta con el nodo de atras
                        node.next = newNode;
                        newNode.prev = node;
                        return True
                    node = node.next;
                #Si termina el bucle, se agrega al final
                newNode.prev = node;
                node.next = newNode;
        else:
            self.head = newNode;

    def pop (self):
        #Si tiene elementos
        if(self.head):
            value = self.head.value;
            key = self.head.key;
            self.head = self.head.next;
            if(self.head):
                self.head.prev = None;
            self.length -= 1;
            return value, key;
    
    def enqueue (self, value, key = None):
        oNode = self.Node(value, key);
        if(self.head):
            self.head.prev = oNode;
            oNode.next = self.head;
            self.head = oNode;
        else:
            self.head = oNode;
            self.tail = oNode;
        self.length += 1;
    
    def dequeue (self):
        #Si tiene elementos
        if(self.head):
            value = self.tail.value;
            key = self.tail.key;
            self.tail = self.tail.prev;
            if(self.tail):
                self.tail.next = None;
            else:
                self.head = None;
            self.length -= 1;
            return value, key;
    
    def show (self):
        currentNode = self.head;
        sString = "["
        while (currentNode != None):
            sString += str(currentNode.value) + ", ";
            currentNode = currentNode.next;
        sString = sString[: len(sString) - 2];
        if(len(sString) > 0):
            sString += "]";
            print(sString);
        else:
            print("No hay elementos en la lista");

    def exist (self, L):
        node = self.head;
        Lnode = L.head;
        #Las listas tienen elementos
        if(node and Lnode):
            #Si la lista que ingresa tiene menos elementos que la que estamos analizando:
            if(L.lenght() < self.lenght()):
                while (node != None):
                    if(node.value != Lnode.value):
                        return False
                    node = node.next;
                    Lnode = Lnode.next;
                return True
        return False

    def lenght(self):
        return self.length;