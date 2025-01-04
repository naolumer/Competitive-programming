
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        s,f = head,head

        if not head:
            return False
        while f and f.next:
            s = s.next
            f = f.next.next

            if f==s:
                return True
        return False