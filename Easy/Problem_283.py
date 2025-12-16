class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        w = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[w] = nums[i]
                w += 1
        for i in range(w,n):
            nums[i] = 0
         