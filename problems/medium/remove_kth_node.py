class Solution(object):
    def removeNthFromEnd(self, head, n):
        p = head
        count = 0
        while p:
            count +=1
            p = p.next
        removeAt = count - n + 1
        count = 0
        p = head
        prev = None
        while p:
            count += 1
            if removeAt == count:
                if prev == None:
                    return head.next
                if not p.next:
                    prev.next = None
                else:
                    prev.next = p.next
                break
            else:
                prev = p
                p = p.next
        return head