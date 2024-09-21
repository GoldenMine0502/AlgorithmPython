N = int(input())

sum = 0

# 123 자리수의 합 = 6
# 123 % 10 -> 3 +
# 123 / 10 -> 12
# 12 % 10 -> 2 +
# 12 / 10 -> 1
# 1 % 10 -> 1 +
# 1 / 10 -> 0

# 7 % 4 -> 1, 3

while N > 0:
    sum += N % 10
    N //= 10

print(sum)

# find = False
#
# # 216 -> 207, 198
# for i in range(1, N):
#     current = i
#     sum = 0  # 245 -> 2 + 4 + 5 = 11
#
#     while current > 0:
#         sum += current % 10
#         current //= 10
#
#     if sum + i == N:
#         print(i)
#         find = True
#         break
#
# if not find:
#     print(0)

