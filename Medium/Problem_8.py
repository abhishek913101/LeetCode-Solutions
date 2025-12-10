class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        num = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        OVERFLOW_FLAG = INT_MAX // 10
        for char in s:
            if not char.isdigit():
                break
            digit = int(char)
            if num > OVERFLOW_FLAG or (num == OVERFLOW_FLAG and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
        return sign * num