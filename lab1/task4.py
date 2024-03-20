def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        d, x, y = extended_gcd(b, a % b)
        return (d, y, x - (a // b) * y)

def diophantine(a, b, c):
    gcd, x0, y0 = extended_gcd(a, b)
    if c % gcd != 0:
        return "Нет решений"
    else:
        k = c // gcd
        x = x0 * k
        y = y0 * k
        return (x, y)


a = 5
b = 7
c = 14
solution = diophantine(a, b, c)
print("Решение", a, "x +", b, "y =", c, ":")
print(f"Частное решение:\nx = {solution[0]}\ny = {solution[1]}")
print(f"x(k)={solution[0]}{'+' if b >= 0 else ''}{b}k")
print(f"y(k)={solution[1]}{'+' if a < 0 else '-'}{a}k")

