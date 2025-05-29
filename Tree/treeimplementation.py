class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def countofleafnodes(self,root):
        if root is None :
            return 0
        elif root.left is None and root.right is None:
            return 1
        return self.countofleafnodes(root.left)+self.countofleafnodes(root.right)
    def SumofEvennodes(self,root):
        if root :
            return (root.data if root.data%2==0 else 0) + self.SumofEvennodes(root.left) +self.SumofEvennodes(root.right)
        else:
            return 0
    def Sumofnodes(self,root):
        if root :
            return root.data+ self.Sumofnodes(root.left) +self.Sumofnodes(root.right)
        else:
            return 0
    def PostOrderTraversal(self,root):
        if root:
            self.PostOrderTraversal(root.left)
            self.PostOrderTraversal(root.right)
            print(root.data,end=" ")
        else:
            return 
    def PreOrderTraversal(self,root):
        if root:
            print(root.data,end=" ")
            self.PreOrderTraversal(root.left)
            self.PreOrderTraversal(root.right)
        else:
            return 
    def InOrderTraversal(self,root):
        if root:
            self.InOrderTraversal(root.left)
            print(root.data,end=" ")
            self.InOrderTraversal(root.right)
        else:
            return 
    def HeightofTree(self,root):
        if root :
            return 1+max(self.HeightofTree(root.right),self.HeightofTree(root.left))
        else:
            return -1
    def SearchNode(self,root,val):
        if root:
            if root.data==val:
                return True
            return self.SearchNode(root.left,val) or self.SearchNode(root.right,val)
        else:
            return False
    def NagarajSearch(self,root,val):
        if root is None:
            return False
        elif root.data==val:
            return True
        elif root.data>val:
            return self.NagarajSearch(root.left,val)
        else:
            return self.NagarajSearch(root.right,val) 
    def printpaths(self, root):
        if root is None:
            return []

        if root.left is None and root.right is None:
            return [[root.data]]

        paths = []
        left_paths = self.printpaths(root.left)
        right_paths = self.printpaths(root.right)

        for path in left_paths + right_paths:
            paths.append([root.data] + path)
        
        return paths
    # def leftview(self,root,c):
    #     if root is None:
    #         return 
    #     if c not in d:
    #         d[c]=root.data
    #     self.leftview(root.left)
    #     self.leftview(root.right)


mytree=Tree(10) 
mytree.left=Node(5)
mytree.right=Node(20)
mytree.left.left=Node(2)
mytree.left.right=Node(8)
mytree.right.left=Node(12)
mytree.right.right=Node(25)
print("InOrder Traversal :",end=" ")
mytree.InOrderTraversal(mytree)
print()
print("Preorder Traversal :",end=" ")
mytree.PreOrderTraversal(mytree)
print()
print("Post order Traversal :",end=" ")
mytree.PostOrderTraversal(mytree)
print()
print(f"Sum of Nodes is : {mytree.Sumofnodes(mytree)}")
print(f"Sum of Even Nodes is : {mytree.SumofEvennodes(mytree)}")
print(f"The Height of Tree is : {mytree.HeightofTree(mytree)}")
val=8
print(f"The element {val} is there in tree : {mytree.SearchNode(mytree,val)}")
print(f"The element {val} is there in tree : {mytree.NagarajSearch(mytree,val)}")
print(f"The number of leaf nodes is {mytree.countofleafnodes(mytree)}")
print(f"The number of leaf nodes is {mytree.printpaths(mytree)}")
