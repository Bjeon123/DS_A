class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
	pointer = linkedList
	prev = None
	while pointer.next:
		if pointer.value == pointer.next.value:
			if prev == None:
				linkedList = pointer.next
				pointer = linkedList
			else:
				prev.next = pointer.next
				pointer = pointer.next
		else:		
			prev = pointer
			pointer = pointer.next
    return linkedList
