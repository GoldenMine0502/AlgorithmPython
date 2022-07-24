import sys


# 입력 받기
lines = []

for i in range(0, int(input())):
    lines.append(sys.stdin.readline().rstrip())


# solve
def solve(line):
    stack = []

    for index in range(0, len(line)):
        ch = line[index]

        if len(stack) > 0:
            top = stack[-1]

            if ch == top:
                stack.pop()
            else:
                stack.append(ch)
        else:
            stack.append(ch)

    return len(stack) == 0


count = 0
for i in range(0, len(lines)):
    succeed = solve(lines[i])
    if succeed:
        count = count + 1

print(count)


