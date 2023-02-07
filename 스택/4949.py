while(True):
    array = input()
    stack = []

    if array == '.':
        break
    for _ in array:
        if (_ == "(") or (_ == "["):
            stack.append(_)
        elif _ == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")")
        elif _ == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append("]")
    if len(stack) == 0:
        print("yes")
    else:
        print("no")
