class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        length = len(s)
        s2 = []
        ans = float('-inf')
        # ans = 0   #1
        if length == 0:
            return 0
        elif length == 1:
            return 1
        else:
            for i in range(len(s)):
                if s[i] not in s2:
                    s2.append(s[i])
                else:
                    while s[i] in s2: 
                        l = 1
                        s2 = s2[l:]
                    s2.append(s[i])
                ans = max(ans,len(s2)) #3

        return ans