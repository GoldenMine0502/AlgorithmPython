def gcd_recursive(x, y):
    if y == 0:
        return x
    else:
        return gcd_recursive(y, x % y)


def gcd_loop(p, q):
    while q:
        p, q = q, p % q

    return p


print(gcd_recursive(12, 8))
print(gcd_loop(12, 8))
print(gcd_recursive(72, 60))
print(gcd_loop(72, 60))
