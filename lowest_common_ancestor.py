"""
You are given pointer to the root of the binary search tree 
and two values and . 
You need to return the lowest common ancestor (LCA) of and in the binary search tree. 

"""

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
  #Enter your code here
  if root is None: return
  if (root.info < v1 and root.info < v2):
    return lca(root.right, v1, v2)
  elif(root.info > v1 and root.info > v2):
    return lca(root.left, v1, v2)
  else:
    return root
  
#   iterative
# def lca(root, v1, v2):

#     current = root
#     while current:
#     # compare our current node to v1 and v2
#     # if both v1 and v2 are to the left, then move left
#     if v1 < current.info and v2 < current.info:
#       current = current.left
#     # if they're both to the right, then move right
#     elif v1 > current.info and v2 > current.info:
#       current = current.right
#     # if neither of those, so one is left and one is right, then we've found our LCA
#     else: 
#       return current

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)

# Time O(n) worst O(log n) best
# Space O(n)