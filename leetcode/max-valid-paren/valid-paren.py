# Leetcode 32

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        parens = [-1]
        max_valid = 0

        for i in range(len(s)):
            if s[i] == "(":
                parens.append(i)
            else:
                parens.pop()
                if not len(parens):
                    parens.append(i)
                else:
                    max_valid = max(max_valid, i - parens[-1])

        return max_valid