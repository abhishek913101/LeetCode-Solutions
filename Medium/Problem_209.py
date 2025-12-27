class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        win_sum = 0
        l = 0
        c = 0
        for i in range(len(nums)):
            win_sum += nums[i]
            while win_sum >= target:
                c += 1
                min_len = min(min_len,i-l+1)
                win_sum -= nums[l]
                l += 1
        if c == 0:
            return 0
        return min_len

