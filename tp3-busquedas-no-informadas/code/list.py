from typing import Deque


class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value;
            self.next = None;
            self.prev = None;
    def __init__(self):
        self.head = None;
        self.tail = None;
        self.length = 0;
    
    def push (self, value):
        oNode = self.Node(value);
        #Si no tiene header
        if(not self.head):
            self.head = oNode;
            self.tail = oNode;
        else:
            oNode.prev = self.tail;
            self.tail.next = oNode;
            self.tail = oNode;
        self.length += 1;
    
    def pop (self):
        #Si tiene elementos
        if(self.head):
            value = self.tail.value;
            self.tail = self.tail.prev;
            if(self.tail):
                self.tail.next = None;
            else:
                self.head = None;
            self.length -= 1;
            return value;
    
    def enqueue (self, value):
        oNode = self.Node(value);
        if(not self.head):
            self.head = oNode;
            self.tail = oNode;
        else:
            self.head.prev = oNode;
            oNode.next = self.head;
            self.head = oNode;
        self.length += 1;
    
    def dequeue (self):
        return self.pop();
    
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

    def lenght(self):
        return self.length;