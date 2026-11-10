# Leetcode 150

from math import floor, ceil

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        eval_stack = []

        for tok in tokens:
            if tok[-1].isdigit():
                eval_stack.append(int(tok))
                continue

            l = eval_stack.pop()
            r = eval_stack.pop()

            if tok == "+":
                result = r + l
            elif tok == "-":
                result = r - l
            elif tok == "*":
                result = r * l
            else:
                # **always** truncates toward zero
                result = (
                    ceil(raw_r)
                    if (raw_r := r / l) and raw_r < 0
                    else floor(raw_r)
                )

            eval_stack.append(result)

        return eval_stack[0]