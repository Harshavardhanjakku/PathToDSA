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
    def contiguosparisk(self,k):
        temp=self.head
        c=0
        while temp.next.next:
            if (temp.data +temp.next.data)<=k:
                c+=1
            temp=temp.next
        return c 
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
print(f"Total nodes leass than 6 is {obj.contiguosparisk(8)}")
