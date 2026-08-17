# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # get the head
        node = head

        # the tail will point to null
        # so will the first node if reversed
        previous_node = None
        
        # while pointing to something
        while node:
            # next node
            next_node = node.next

            # make the current node point to previous node, (first iteration point to Null)
            node.next = previous_node
            
            # previous node now becomes this node
            previous_node = node

            # current node becomes next node
            node = next_node

        #return
        return previous_node

           
        
            