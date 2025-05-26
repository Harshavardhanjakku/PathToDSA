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
    def sumofallnodesEven(self):
        temp=self.head
        s=0
        while temp:
            if temp.data%2==0:
                s+=temp.data
            temp=temp.next
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
obj.sumofallnodesEven()