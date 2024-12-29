# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:    # checking if the head is empty or null
            return head
        N = 1
        cur = head
        while cur.next:     # counting the length of our linkedlist
            N+=1
            cur = cur.next
        cur.next = head     # making the linkedlist circular (connection the tail to the head)
        M = N- k%N          # do the modulo operation to prevent redundancy
        
        cur = head
        i=0
        while i < M:
            prev = cur 
            cur = cur.next
            i+=1                # move the head to M position
        prev.next = None        
        head = cur
        

        return head