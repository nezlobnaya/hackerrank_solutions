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
def height(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 0
    return (1 + max(height(root.left), height(root.right)))
    
    

# Iterative function to calculate height of given binary tree
# by doing level order traversal of the tree
# def height(root):
 
#     # empty tree has height 0
#     if root is None:
#         return 0
 
#     # create an empty queue and enqueue root node
#     queue = deque()
#     queue.append(root)
 
#     height = 0
 
#     # loop till queue is empty
#     while queue:
 
#         # calculate number of nodes in current level
#         size = len(queue)
 
#         # process each node of current level and enqueue their
#         # non-empty left and right child to queue
#         while size > 0:
#             front = queue.popleft()
 
#             if front.left:
#                 queue.append(front.left)
 
#             if front.right:
#                 queue.append(front.right)
 
#             size = size - 1
 
#         # increment height by 1 for each level
#         height = height + 1
 
#     return height

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))
