

# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(llist, data):
    if llist==None:
        return SinglyLinkedListNode(data)
    node=SinglyLinkedListNode(data)
    node.next=llist
    return node

