from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root=None):
        self.root = root

    def Insert(self, root, x):
        if root is None:
            return Node(x)
        elif x < root.data:
            root.left = self.Insert(root.left, x)
        else:
            root.right = self.Insert(root.right, x)
        return root

    def SumofEvennodes(self, root):
        if root:
            return (root.data if root.data % 2 == 0 else 0) + \
                   self.SumofEvennodes(root.left) + self.SumofEvennodes(root.right)
        else:
            return 0

    def Sumofnodes(self, root):
        if root:
            return root.data + self.Sumofnodes(root.left) + self.Sumofnodes(root.right)
        else:
            return 0

    def PostOrderTraversal(self, root):
        if root:
            self.PostOrderTraversal(root.left)
            self.PostOrderTraversal(root.right)
            print(root.data, end=" ")

    def PreOrderTraversal(self, root):
        if root:
            print(root.data, end=" ")
            self.PreOrderTraversal(root.left)
            self.PreOrderTraversal(root.right)

    def InOrderTraversal(self, root):
        if root:
            self.InOrderTraversal(root.left)
            print(root.data, end=" ")
            self.InOrderTraversal(root.right)

    def HeightofTree(self, root):
        if root:
            return 1 + max(self.HeightofTree(root.left), self.HeightofTree(root.right))
        else:
            return -1  # height of leaf is considered 0

    def SearchNode(self, root, val):
        if root:
            if root.data == val:
                return True
            return self.SearchNode(root.left, val) or self.SearchNode(root.right, val)
        else:
            return False

    def NagarajSearch(self, root, val):
        if root is None:
            return False
        elif root.data == val:
            return True
        elif root.data > val:
            return self.NagarajSearch(root.left, val)
        else:
            return self.NagarajSearch(root.right, val)
        
    def Levelordertraaversal(self, root):
        if root is None:
            return
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            print(node.data, end=" ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    def Countnodesusingtraversal(self, root):
        c=0
        if root is None:
            return c
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            print(node.data, end=" ")
            if node.left is None and node.right is None :
                c+=1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return c

        
mytree = Tree()
values = [10, 5, 20, 2, 8, 12, 25]
for v in values:
    mytree.root = mytree.Insert(mytree.root, v)

print("InOrder Traversal :", end=" ")
mytree.InOrderTraversal(mytree.root)
print()

print("PreOrder Traversal :", end=" ")
mytree.PreOrderTraversal(mytree.root)
print()

print("PostOrder Traversal :", end=" ")
mytree.PostOrderTraversal(mytree.root)
print()

print(f"Sum of Nodes is : {mytree.Sumofnodes(mytree.root)}")
print(f"Sum of Even Nodes is : {mytree.SumofEvennodes(mytree.root)}")
print(f"The Height of Tree is : {mytree.HeightofTree(mytree.root)}")

val = 8
print(f"The element {val} is there in tree : {mytree.SearchNode(mytree.root, val)}")
print(f"The element {val} is there in tree (BST Search) : {mytree.NagarajSearch(mytree.root, val)}")
mytree.Levelordertraaversal(mytree.root)
mytree.Countnodesusingtraversal(mytree.root)
