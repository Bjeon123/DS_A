import sys

def findClosestValueInBst(tree, target):
    return bfs(tree, sys.maxsize, target)

def bfs(node, closest_val, target):
	closest_val = node.value if abs(target) - abs(node.value) < abs(closest_val) - abs(target) else closest_val
	if (not node.left and not node.right) or (target < node.value and not node.left) or (target > node.value and not node.right):
		return closest_val
	if target < node.value:
		return bfs(node.left, closest_val, target)
	elif target > node.value:
		return bfs(node.right, closest_val, target)
	


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None