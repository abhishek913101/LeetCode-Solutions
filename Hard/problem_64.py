class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        seen_digit = False
        seen_dot = False
        seen_e = False
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char in ('+', '-'):
                if i > 0 and s[i-1] != 'e' and s[i-1] != 'E':
                    return False
            elif char == '.':
                if seen_dot or seen_e:
                    return False
                seen_dot = True
            elif char in ('e', 'E'):
                if seen_e or not seen_digit:
                    return False
                seen_e = True
                seen_digit = False
            else:
                return False
        return seen_digit