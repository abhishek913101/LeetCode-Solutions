class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        win_sum = 0
        l = 0
        if sum(nums) < target:
            return 0
        for i in range(len(nums)):
            win_sum += nums[i]
            while win_sum >= target:
                min_len = min(min_len,i-l+1)
                win_sum -= nums[l]
                l += 1
        return min_len

