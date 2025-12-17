class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        d2 = {}
        for ch in magazine:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1
        for ch in ransomNote:
            if ch not in d2:
                d2[ch] = 1
            else:
                d2[ch] += 1
        for v,c in d2.items():
            if c > d.get(v,0):
                return False 
        return True


