class Solution(object):
    def majorityElement(self, nums):
        count = 0;
        most_freq = None
        hmap = {}
        for num in nums:
            if num in hmap:
                hmap[num] += 1
            else:
                hmap[num] = 1
            if hmap[num] > count:
                count = hmap[num]
                most_freq = num
        return most_freq