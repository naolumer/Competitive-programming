# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        cur = head
        lis = [cur.val]
        while  cur.next:
            cur=cur.next
            lis.append(cur.val)
        return lis == lis[::-1]

       