class Solution(object):
    def findLHS(self, nums):
        hMap = {}
        longest = 0
        for num in nums:
            if num in hMap:
                hMap[num] += 1
            else:
                hMap[num] = 1
            if hMap.has_key(num) and hMap.has_key(num + 1):
                subSeqLen = hMap[num] + hMap[num + 1]
                if subSeqLen > longest:
                    longest = subSeqLen
            if hMap.has_key(num) and hMap.has_key(num - 1):
                subSeqLen = hMap[num] + hMap[num - 1]
                if subSeqLen > longest:
                    longest = subSeqLen
        return longest
