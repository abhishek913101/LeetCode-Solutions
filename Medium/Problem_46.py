class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        def backtrack(current_permutation, remaining_nums):
            if len(current_permutation) == n:
                result.append(list(current_permutation))
                return
            for i in range(len(remaining_nums)):
                num = remaining_nums[i]
                new_remaining = remaining_nums[:i] + remaining_nums[i+1:]
                backtrack(current_permutation + [num], new_remaining)
        backtrack([], nums)
        return result