def reverseList(head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev,curr = None,head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
