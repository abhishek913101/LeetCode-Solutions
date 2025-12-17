class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for ch in s:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1
        for i,j in d.items():
            if j == 1:
                return s.index(i)
        else:
            return -1
        