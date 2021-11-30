def nodeDepths(root):
    	return calcDepthSum(root, 1)
	
def calcDepthSum(node, currDepth):
	sumDepth = 0
	if node.left:
		sumDepth += currDepth
		sumDepth += calcDepthSum(node.left, currDepth +1)
	if node.right:
		sumDepth += currDepth
		sumDepth += calcDepthSum(node.right, currDepth +1)
	return sumDepth
		
	


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None