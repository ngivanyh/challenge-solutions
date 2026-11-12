# Leetcode 20

class Solution:
    def isValid(self, s: str) -> bool:
        paren_stack = ["\0"]
        for c in s:
            top = paren_stack[-1]

            if (
                (c == ")" and top == "(")
                or (c == "]" and top == "[")
                or (c == "}" and top == "{")
            ):
                paren_stack.pop()
            else:
                paren_stack.append(c)

        return paren_stack[-1] == "\0"
