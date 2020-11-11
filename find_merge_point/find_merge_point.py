"""
Given pointers to the head nodes of linked lists that merge together at some point, find the node where the two lists merge. The merge point is where both lists point to the same node, i.e. they reference the same memory location. It is guaranteed that the two head nodes will be different, and neither will be NULL. If the lists share a common node, return that node's

value.

Note: After the merge point, both lists will share the same node pointers. 
"""


def findMergeNode(head1, head2):
    ptr1, ptr2 = head1, head2
    while ptr1 and ptr2:
        if ptr1 == ptr2:
            break
        ptr1 = ptr1.next
        ptr2 = ptr2.next
        
        if ptr1 == None:
            ptr1 = head1
        if ptr2 == None:
            ptr2 = head2
    return ptr1.data
        

