"""
    non recursive solution
"""

def mergeLists(head1, head2):

    if not head1 : return head2
    if not head2 : return head1

    # Starting here, both <head1> and <head2> are not None.
    m = int( head1.data > head2.data ) # 0 if False; 1 if True
    head = [head1, head2] ; head_merge = head[m]

    # <precursor> denotes the last node of the merged linked list.
    precursor, cursor = head_merge, head
    cursor[m] = precursor.next

    while precursor:
        if not cursor[m]:
            precursor.next = cursor[1-m] ; break
        else:
            m = int( cursor[0].data > cursor[1].data )
            precursor.next, cursor[m] = cursor[m], cursor[m].next
        precursor = precursor.next
        
    return head_merge

"""
 recursive solution
"""

import sys

sys.setrecursionlimit(10000) 
def mergeLists(head1, head2):
  if head1 is None and head2 is None:
    return None
  
  if head1 is None:
    return head2

  if head2 is None:
    return head1
  
  if head1.data < head2.data:
    smallerNode = head1
    smallerNode.next = mergeLists(head1.next, head2)
  else:
    smallerNode = head2
    smallerNode.next = mergeLists(head1, head2.next)
  
  return smallerNode