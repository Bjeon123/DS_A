class Solution(object):
    def mergeTwoLists(self, list1, list2):
        ll = ListNode()
        p = ll
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    ll.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    ll.next = ListNode(list2.val)
                    list2 = list2.next
            elif list1:
                ll.next = ListNode(list1.val)
                list1 = list1.next
            else:
                ll.next = ListNode(list2.val)
                list2 = list2.next
            ll = ll.next
        return p.next