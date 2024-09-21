def minOperationsToMakeEmpty(S):
    count = 0
    stack = []

    for char in S:
        if stack and char != stack[-1]:
            stack.pop()
            count += 2
        else:
            stack.append(char)

    return count

# 예제 입력
S = "0101110100"
result = minOperationsToMakeEmpty(S)
print(result)  # 4

# 0101110100
#   01110100
#   011  100
#     1  100
#          x -> 4회

# 0111000011
# 0      011

# 0101110001

# 011000111100
# 00001110010111
