expr = input()

postfix = ""
op_stack = []

precedence = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
}

for c in expr:
    # print(op_stack, f"\"{postfix}\"")
    if "A" <= c <= "Z":
        postfix += c
    elif c == "(":
        op_stack.append("(")
    elif c in precedence.keys():
        while op_stack and op_stack[-1] != "(" and precedence[op_stack[-1]] >= precedence[c]:
            postfix += op_stack.pop()
            # print("Precedence pops: ", op_stack, f"\"{postfix}\"")
        op_stack.append(c)
    else:
        while op_stack and op_stack[-1] != "(":
            postfix += op_stack.pop()
            # print("Bracket pops: ", op_stack, f"\"{postfix}\"")
        op_stack.pop()

while op_stack:
    postfix += op_stack.pop()

print(postfix)