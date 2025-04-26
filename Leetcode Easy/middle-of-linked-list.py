def middleNode(head):
    fastp= head
    slowp = head

    while fastp and fastp.next:
        slowp = slowp.next
        fastp = fastp.next.next
    return slowp