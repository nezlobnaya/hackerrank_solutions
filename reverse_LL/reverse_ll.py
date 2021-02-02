

# Complete the reverse function below.

#
# For your reference:
#
from typing import List, Set, Dict, Tuple, Optional
class SinglyLinkedListNode:
    int data
    SinglyLinkedListNode next
#
#
def reverse(head):
    prev, current = None, head
    while current:
        prev, current.next, current = current, prev, current.next
    return prev
  

