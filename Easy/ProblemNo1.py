class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i,num in enumerate(nums):
            d[num]=i
        for i,num in enumerate(nums):
            desire = target-num
            if desire in d and d[desire] != i:
                return [i,d[desire]]
        
