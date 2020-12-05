"""
For the purposes of this challenge, we define a binary tree to be a binary search tree with the following ordering requirements:

    The 

value of every node in a node's left subtree is less than the data value of that node.
The value of every node in a node's right subtree is greater than the data value of that node.

Given the root node of a binary tree, can you determine if it's also a binary search tree? 

"""



class Node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

# def check_binary_search_tree_(root, left = None, right = None):
#     if root is None: return True
    
#     if left and left.data >= root.data: return False
#     if right and right.data <= root.data: return False
    
#     return check_binary_search_tree_(root.left, left, root) and check_binary_search_tree_(root.right, root, right)

def solve (root, min_val, max_val ):
    if root is None or root.data == 0: return True
    if (root.data <= min_val or root.data >= max_val):return False
    return solve(root.left, min_val, root.data) and solve(root.right, root.data, max_val)
def check_binary_search_tree_(root):
    return solve(root,float("-inf"), float("inf") )



if __name__ == '__main__': 
    root = Node(3)  
    root.left = Node(2)  
    root.right = Node(5)  
    root.right.left = Node(1)  
    root.right.right = Node(4)  
    root.right.left.left = Node(40) 
    if (check_binary_search_tree_(root)): 
        print("Is BST") 
    else: 
        print("Not a BST")    
  