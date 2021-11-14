class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
	size = 0
	pointer = head
	while pointer:
		size += 1
		pointer = pointer.next
	i = 1
	pointer = head
	print(size-k)
	while i < size -k :
		pointer = pointer.next
		i +=1
	if pointer == head:
		head = head.next
		print(head.next.value)
	else:
		pointer.next = pointer.next.next
	print(size)
