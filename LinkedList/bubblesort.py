class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insertAtEnd(self,data):
        newnode=Node(data)
        temp=self.head
        if temp is None :
            self.head=newnode
            return 
        while temp.next:
            temp=temp.next
        temp.next=newnode
    def sortll(self):
        if self.head is None or self.head.next is None:
            return
        flag = True
        while flag:
            flag = False
            current = self.head
            while current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    flag = True
                current = current.next

    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
obj=LinkedList()
obj.insertAtEnd(3)
obj.insertAtEnd(2)
obj.insertAtEnd(7)
obj.insertAtEnd(1)
obj.insertAtEnd(6)
obj.sortll()
obj.display()