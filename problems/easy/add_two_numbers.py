class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        solution = None
        p = solution
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            sum = carry;
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            carry = sum / 10
            if not solution:
                solution = ListNode(sum % 10)
                p = solution
            else: 
                node = ListNode(sum % 10)
                p.next = node
                p = p.next
        return solution