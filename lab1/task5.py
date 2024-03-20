import math


def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = gcd_extended(b % a, a)
        return gcd, y - (b // a) * x, x

def mod_inverse(a, m):
    gcd, x, y = gcd_extended(a, m)
    if gcd != 1:
        raise Exception(f"The inverse of {a} modulo {m} does not exist.")
    else:
        return x % m

def solve_linear_congruence(a, b, m):
    gcd = math.gcd(a, m)
    if b % gcd != 0:
        raise Exception("No solutions")
    else:
        a = a // gcd
        b = b // gcd
        m = m // gcd
        inverse = mod_inverse(a, m)
        solution = (inverse * b) % m
        return solution

# Сравнение: 3x ≡ 19 (mod 34)
a = 3
b = 19
m = 34

# Решение сравнения первым способом
x_inv = mod_inverse(a, m)
solution_1 = (x_inv * b) % m

# Решение сравнения вторым способом
solution_2 = solve_linear_congruence(a, b, m)

print("Первый способ:", solution_1)
print("Второй способ:", solution_2)
