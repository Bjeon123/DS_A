class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        currentNode = self.head
        while(currentNode.next is not None):
            currentNode = currentNode.next
        currentNode.next = Node(data)

    def insert_values(self, data_arr):
        currentNode = self.head
        for data in data_arr:
            node = Node(data)
            if currentNode is None:
                self.head = node
                currentNode = node
            else:
                currentNode.next = node
                currentNode = currentNode.next


    def get_length(self):
        counter = 0
        p = self.head
        while(p is not None):
            counter +=1
            p = p.next
        print(counter)

    def remove_at(self, index):
        counter = 0
        p = self.head
        prev = None
        if index == 0:
            self.head = self.head.next
            print("Node Deleted at index" + str(index) +": data: " + str(p.data))
            return 
        while(p is not None):
            if(counter == index):
                prev.next = p.next
                print("Node Deleted at index" + str(index) +": data: " + str(p.data))
                return
            else:
                counter +=1
                prev = p
                p = p.next
        print("index out of bounds")

    def print(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            currentNode = self.head
            ll_str = ""
            while(currentNode is not None):
                ll_str += str(currentNode.data) + "-->"
                currentNode = currentNode.next
            print(ll_str)



if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_at_front(10)
    # ll.insert_at_front(11)
    # ll.insert_at_end(3)
    ll.insert_values(["apple", "bannana", "kiwi", "berry"])
    ll.remove_at(0)
    ll.print()
    ll.get_length()
     
        