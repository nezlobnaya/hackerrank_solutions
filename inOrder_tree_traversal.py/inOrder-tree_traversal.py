from collections import deque
def inOrder(root):
    #Write your code here
    # if root:
    #     inOrder(root.left)
    #     print(root.info, end = " ")
    #     inOrder(root.right)
    # else: return



    if not root:
        return 
    res = deque()
    cur = root
    while cur or res:
        if cur:
            res.append(cur)
            cur = cur.left
        else:
            cur = res.pop()
            print(cur.info, end=" ")
            cur = cur.right
            