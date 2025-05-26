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
    def countnodes(self):
        temp=self.head
        c=0
        while temp:
            c+=1
            temp=temp.next
        return c
    def Kthelementfromlast(self,k):
        n=self.countnodes()
        i=0
        temp=self.head
        while i<n-k:
            temp=temp.next
            i+=1
        print(f"Kth element from last is {temp.data}")
    def kthlastelementfromlast(self,k):
        fast=self.head
        i=1
        while i<=k:
            i+=1
            fast=fast.next
        slow=self.head
        while fast :
            slow=slow.next
        print(slow.data)
    def display(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
obj=LinkedList()
obj.insertAtEnd(3)
obj.insertAtEnd(2)
obj.insertAtEnd(7)
obj.insertAtEnd(1)
obj.insertAtEnd(6)
obj.Kthelementfromlast(5)
obj.Kthelementfromlast(2)
obj.display()