class Solution(object):   
    def isSameTree(self, p, q):
        first = self.bfs(p)
        second = self.bfs(q)
        print(first)
        print(second)
        return first == second
    
    def bfs(self, root):
        if not root:
            return []
        traversal = []
        traversal.append(root.val)
        if root.left:
            traversal += self.bfs(root.left)
        else:
            traversal.append(None)
        if root.right:
            traversal += self.bfs(root.right)
        else:
            traversal.append(None)
        return traversal