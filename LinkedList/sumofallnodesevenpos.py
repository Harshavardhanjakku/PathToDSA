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
    def sumofallnodesEvenPosition(self):
        temp=self.head.next
        s=0
        while temp:
            s+=temp.data
            temp=temp.next.next
        print(f"Sum of all Even nodes {s}")
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
obj.display()
obj.sumofallnodesEvenPosition()