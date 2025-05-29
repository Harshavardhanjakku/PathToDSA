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
    def insertAtPosition(self, data, pos):
        newnode = Node(data)
        if pos == 1:
            newnode.next = self.head
            self.head = newnode
            return
        temp = self.head
        i = 1
        while temp is not None and i < pos - 1:
            temp = temp.next
            i += 1
        if temp is None:
            print(f"Cannot insert at position {pos}: position out of bounds.")
            return
        newnode.next = temp.next
        temp.next = newnode
    def findlooplength(self):
        if not self.head or not self.head.next:
            return 0  
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                count = 0
                slow = slow.next  
                while slow != fast:
                    count += 1
                    slow = slow.next
                return count + 1  
        return 0  
    def insertAtbegin(self,data):
        newnode=Node(data)
        temp=self.head
        newnode.next=self.head
        self.head=newnode
        return
    def display(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
obj=LinkedList()
obj.insertAtbegin(12)
obj.insertAtEnd(3)
obj.insertAtEnd(2)
obj.insertAtEnd(7)
obj.insertAtEnd(1)
obj.insertAtEnd(6)
obj.insertAtPosition(9,3)
obj.insertAtbegin(-1)
obj.display()
obj.findlooplength()