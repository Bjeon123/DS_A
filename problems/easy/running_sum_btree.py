class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
	return runningSum(root, 0)
	
def runningSum(node, curr_sum):
	running_sums = [] 
	curr_sum += node.value
	if node.left:
		running_sums += runningSum(node.left, curr_sum)
	if node.right:
		running_sums += runningSum(node.right, curr_sum)
	if not node.left and not node.right:
		return [curr_sum]
	return running_sums