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
    def traverseuptomid(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        self.display(slow)
    def display(self,mynode):
        temp=mynode
        while temp:
            print(temp.data)
            temp=temp.next
obj=LinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtEnd(50)
obj.insertAtEnd(60)
obj.traverseuptomid()