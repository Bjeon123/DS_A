class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        s = set()
        pointer = head
        while pointer != None:
            if hex(id(pointer)) in s:
                return True
            else:
                s.add(hex(id(pointer)))
            pointer = pointer.next
        print(set)
        return False