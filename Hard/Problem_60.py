class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        nums = [i + 1 for i in range(n)]
        result = []
        
        for i in range(n - 1, -1, -1):
            fact = math.factorial(i)
            index = k // fact
            k %= fact
            result.append(str(nums[index]))
            nums.pop(index)
            
        return "".join(result)