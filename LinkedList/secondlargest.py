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
    def secondlargest(self):
        if self.head is None or self.head.next is None:
            print("List has fewer than 2 elements.")
            return None

        first = second = float('-inf')
        temp = self.head

        while temp:
            if temp.data > first:
                second = first
                first = temp.data
            elif temp.data > second and temp.data != first:
                second = temp.data
            temp = temp.next

        if second == float('-inf'):
            print("No second largest element found (all elements are equal).")
            return None
        return second

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
print(f"The second largest is  {obj.secondlargest()}")