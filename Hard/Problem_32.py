class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = [-1]  # Initialize the stack with a base index

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    current_length = i - stack[-1]
                    max_len = max(max_len, current_length)

        return max_len