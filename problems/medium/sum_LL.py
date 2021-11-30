class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    sumLL = LinkedList(None)
	p = sumLL
	carry = 0
	while linkedListOne or linkedListTwo or carry != 0:
		currSum = 0
		if linkedListOne and linkedListTwo:
			currSum  = carry + linkedListOne.value + linkedListTwo.value
			linkedListOne = linkedListOne.next
			linkedListTwo = linkedListTwo.next
		elif linkedListOne:
			currSum  = carry + linkedListOne.value
			linkedListOne = linkedListOne.next
		elif linkedListTwo:
			currSum  = carry + linkedListTwo.value
			linkedListTwo = linkedListTwo.next
		else: 
			currSum  = carry
		carry = currSum // 10
		sumLL.next = LinkedList(currSum % 10)
		sumLL = sumLL.next
    return p.next