class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        needed = collections.Counter(t)
        required = len(t)

        l, r = 0, 0
        min_len = float('inf')
        start = 0

        while r < len(s):
            char_r = s[r]
            if char_r in needed:
                needed[char_r] -= 1
                if needed[char_r] >= 0:
                    required -= 1

            while required == 0:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    start = l

                char_l = s[l]
                if char_l in needed:
                    if needed[char_l] >= 0:
                        required += 1
                    needed[char_l] += 1
                l += 1
            r += 1

        return s[start:start + min_len] if min_len != float('inf') else ""