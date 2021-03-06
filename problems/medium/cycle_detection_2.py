class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        index = 0
        s = f = head
        cycle = False
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                cycle = True
                break
        if not cycle:
            return None
        f = head
        while f != s:
            f = f.next
            s = s.next
        return f
                