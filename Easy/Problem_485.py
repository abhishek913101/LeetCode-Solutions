class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        cal_sum = 0
        for i in nums:
            if i == 0:
                cal_sum = 0
            else:
                cal_sum += i
            max_sum = max(max_sum,cal_sum)
        return max_sum

