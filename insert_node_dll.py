"""


"""

class DoublyLinkedListNode:
    # int data
    # DoublyLinkedListNode next
    # DoublyLinkedListNode prev
    def __init__(self, data): 
        self.data = data  
        self.next = None  
        self.prev = None


#
#

def sortedInsert(head, data):
    new_node = DoublyLinkedListNode(data)
    if head is None:
        return new_node
    # if new node is smaller that the head, insert it at the beginning
    elif head.data > data:
        new_node.next = head
        head.prev  = new_node
        return new_node
    else:  
        head.next = sortedInsert(head.next, data)
        head.next.prev = head
        return head
#O(n) time
#O(1) space

# Option 2
    while head.next:
        head.prev, head.next, head = head.next, head.prev, head.next
    head.next, head.prev = head.prev, None
    
    return head