text = input()

arr = [] # [-1, -1, -1]

# arr[0] -> A가 처음 나오는 위치
# arr[1] -> B가 처음 나오는 위치
for i in range(26):
    arr.append(-1)

# abcd
# i = 0 -> a
# i = 1 -> b
# i = 2 -> c
# i = 3 -> d
# bbbbbb
# a -> 97 - 97 = 0
# b -> 98 - 97 = 1
# c -> 99 - 97 = 2
# d -> 100 - 97 = 3
# 101 102 103 104
# 한글 ->
# ㅎㅏㄴ -> 한
for i in range(0, len(text)):
    ch = text[i]

    index = ord(ch) - ord('a')

    if arr[index] == -1:
        arr[index] = i

# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
for i in range(26):
    print(arr[i], end=' ')

# print(ord("A"))

# for i in range(26):
#     print()

# 아스키코드
# 문자를 -> 숫자랑 1:1대응
# A -> 65
# B -> 66
# C -> 67