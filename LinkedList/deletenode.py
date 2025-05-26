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
    def deleteAtbegin(self):
        if self.head is None:
            print("Stack Underflow")
        else:
            self.head=self.head.next
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()
obj=LinkedList()
obj.insertAtEnd(3)
obj.insertAtEnd(2)
obj.insertAtEnd(7)
obj.insertAtEnd(1)
obj.insertAtEnd(6)
obj.display()
obj.deleteAtbegin()
obj.display()