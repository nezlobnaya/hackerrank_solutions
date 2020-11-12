"""


"""

# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    new_node = DoublyLinkedListNode(data)
    if head is None:
        return new_node
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