

# Complete the reversePrint function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def reversePrint(head):
    if head is None:
        return None
    stack = []
    current = head
    while current:
        stack.append(current.data)
        current = current.next
    while stack:
        print(stack.pop())