class Solution(object):
    def isValid(self, s):
        hmap ={'(': ')','{': '}','[': ']'}
        stack = []
        for char in s:
            if char in hmap:
                stack.append(char)
            else:
                if len(stack)==0  or hmap[stack.pop()] != char:
                    return False
        return len(stack) == 0