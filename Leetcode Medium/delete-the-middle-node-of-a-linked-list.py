class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        fp = head
        sp = head
        prev = None

        if head.next is None:
            return None

        while fp and fp.next:
            prev = sp
            fp = fp.next.next
            sp = sp.next
        
        prev.next = prev.next.next
        return head