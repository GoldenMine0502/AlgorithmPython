
xs = []
ys = []

for i in range(3):
    x, y = map(int, input().split())

    xs.append(x)
    ys.append(y)

# print(xs)
# print(ys)

rx = -1
ry = -1

# [5, 5, 7]
# xs.count(5) -> 2
# xs.count(7) -> 1
for i in range(3):
    if xs.count(xs[i]) == 1:
        rx = xs[i]
    if ys.count(ys[i]) == 1:
        ry = ys[i]

print(rx, ry)
