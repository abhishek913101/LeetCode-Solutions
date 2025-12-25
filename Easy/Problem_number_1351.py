class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        for row in grid:
            for el in row:
                if el < 0:
                    ans += 1
        return ans
        