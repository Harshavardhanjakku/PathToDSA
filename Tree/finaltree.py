from collections import deque

# Define a Node for the Binary Search Tree (BST)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Define the Tree class which includes all the required operations
class Tree:
    def __init__(self, root=None):
        self.root = root

    # Insert a value into the BST
    def Insert(self, root, x):
        if root is None:
            return Node(x)
        elif x < root.data:
            root.left = self.Insert(root.left, x)
        else:
            root.right = self.Insert(root.right, x)
        return root

    # Sum of even-valued nodes in the BST
    def SumofEvennodes(self, root):
        if root:
            return (root.data if root.data % 2 == 0 else 0) + \
                   self.SumofEvennodes(root.left) + self.SumofEvennodes(root.right)
        return 0

    # Sum of all node values in the BST
    def Sumofnodes(self, root):
        if root:
            return root.data + self.Sumofnodes(root.left) + self.Sumofnodes(root.right)
        return 0

    # Postorder traversal (Left -> Right -> Root)
    def PostOrderTraversal(self, root):
        if root:
            self.PostOrderTraversal(root.left)
            self.PostOrderTraversal(root.right)
            print(root.data, end=" ")

    # Preorder traversal (Root -> Left -> Right)
    def PreOrderTraversal(self, root):
        if root:
            print(root.data, end=" ")
            self.PreOrderTraversal(root.left)
            self.PreOrderTraversal(root.right)

    # Inorder traversal (Left -> Root -> Right)
    def InOrderTraversal(self, root):
        if root:
            self.InOrderTraversal(root.left)
            print(root.data, end=" ")
            self.InOrderTraversal(root.right)

    # Height of the tree (leaf has height 0)
    def HeightofTree(self, root):
        if root:
            return 1 + max(self.HeightofTree(root.left), self.HeightofTree(root.right))
        return -1

    # General binary tree search
    def SearchNode(self, root, val):
        if root:
            if root.data == val:
                return True
            return self.SearchNode(root.left, val) or self.SearchNode(root.right, val)
        return False

    # BST-optimized search
    def NagarajSearch(self, root, val):
        if root is None:
            return False
        elif root.data == val:
            return True
        elif val < root.data:
            return self.NagarajSearch(root.left, val)
        else:
            return self.NagarajSearch(root.right, val)

    # Level order traversal (Breadth First Search)
    def Levelordertraaversal(self, root):
        if root is None:
            return
        q = deque([root])
        while q:
            node = q.popleft()
            print(node.data, end=" ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print()

    # Count and print leaf nodes using level order traversal
    def Countnodesusingtraversal(self, root):
        c = 0
        if root is None:
            return c
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left is None and node.right is None:
                c += 1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print(f"\nNumber of leaf nodes: {c}")
        return c

    # Return all paths from root to leaf as a list of lists
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

    # Lowest Common Ancestor using path lists (not optimized)
    def LCA(self, root, p, q):
        path1 = self.findpath(root, p)
        path2 = self.findpath(root, q)
        print(f"Path to {p}: {path1}\nPath to {q}: {path2}")
        min_len = min(len(path1), len(path2))
        lca = -1
        for i in range(min_len):
            if path1[i] == path2[i]:
                lca = path1[i]
            else:
                break
        print(f"LCA of {p} and {q} is: {lca}")

    # Find path from root to a given value
    def findpath(self, root, val):
        path = []
        temp = root
        while temp:
            path.append(temp.data)
            if val < temp.data:
                temp = temp.left
            elif val > temp.data:
                temp = temp.right
            else:
                return path
        return []

    # Optimized LCA for BSTs
    def OptimisedLCA(self, root, p, q):
        if root is None:
            return None
        if root.data > p and root.data > q:
            return self.OptimisedLCA(root.left, p, q)
        elif root.data < p and root.data < q:
            return self.OptimisedLCA(root.right, p, q)
        else:
            return root.data

# Testing all functionalities
mytree = Tree()
values = [40, 10, 50, 5, 20, 45, 55, 2, 7, 15, 22, 6, 8]
for v in values:
    mytree.root = mytree.Insert(mytree.root, v)

print("InOrder Traversal:", end=" ")
mytree.InOrderTraversal(mytree.root)
print("\nPreOrder Traversal:", end=" ")
mytree.PreOrderTraversal(mytree.root)
print("\nPostOrder Traversal:", end=" ")
mytree.PostOrderTraversal(mytree.root)

print(f"\n\nSum of Nodes: {mytree.Sumofnodes(mytree.root)}")
print(f"Sum of Even Nodes: {mytree.SumofEvennodes(mytree.root)}")
print(f"Height of Tree: {mytree.HeightofTree(mytree.root)}")

val = 8
print(f"\nElement {val} exists (General Search): {mytree.SearchNode(mytree.root, val)}")
print(f"Element {val} exists (BST Search): {mytree.NagarajSearch(mytree.root, val)}")

print("\nLevel Order Traversal:")
mytree.Levelordertraaversal(mytree.root)

mytree.Countnodesusingtraversal(mytree.root)

print("\nAll Root-to-Leaf Paths:")
paths = mytree.printpaths(mytree.root)
for path in paths:
    print(" -> ".join(map(str, path)))

print("\nFinding LCA using Path Method:")
mytree.LCA(mytree.root, 8, 22)

print("\nFinding Optimised LCA:")
lca_value = mytree.OptimisedLCA(mytree.root, 2, 8)
print(f"Optimised LCA of 2 and 8 is: {lca_value}")