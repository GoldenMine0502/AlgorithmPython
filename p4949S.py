import sys

strings = []

while True:
    line = sys.stdin.readline().rstrip()
    if line != '.':
        strings.append(line)
        # print(line)
    else:
        break

for i in range(0, len(strings)):
    stack = []
    current = strings[i]
    succeed = True

    for j in range(0, len(current)):
        ch = current[j]

        if ch == '(' or ch == '[':
            stack.append(ch)

        if ch == ')' or ch == ']':
            if len(stack) > 0:
                top = stack.pop()
                # print("top:", top)

                if (top == '(' and ch == ')') or (top == '[' and ch == ']'):
                    pass
                    # succeed = True
                else:
                    succeed = False
                    break
            else:
                succeed = False
                break

    if succeed and len(stack) == 0:
        print("yes")
    else:
        print("no")
