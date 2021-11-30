class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        traversal = []
		traversal.append(self.name)
		for node in self.children:
			traversal += Node.depthFirstSearch(node,array)
		return traversal
			