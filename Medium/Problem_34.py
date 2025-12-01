class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.findBound(nums, target, True)
        right = self.findBound(nums, target, False)
        return [left, right]
        
    def findBound(self, nums: List[int], target: int, findLeft: bool) -> int:
        l, r = 0, len(nums) - 1
        index = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                index = mid
                if findLeft:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return index