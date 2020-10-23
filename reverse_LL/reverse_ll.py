

# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):
    prev, current = None, head
    while current:
        prev, current.next, current = current, prev, current.next
    return prev
  

