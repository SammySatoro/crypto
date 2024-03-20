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
    gcd, x, y = gcd_extended(a, m)
    if b % gcd != 0:
        raise Exception("No solutions")
    else:
        # Одно решение
        if gcd == 1:
            a_reduced = a // gcd
            b_reduced = b // gcd
            m_reduced = m // gcd
            inverse_reduced = mod_inverse(a_reduced, m_reduced)
            single_solution = (inverse_reduced * b_reduced) % m_reduced
            return [single_solution]
        else:
            # Несколько решений
            a_reduced = a // gcd
            b_reduced = b // gcd
            m_reduced = m // gcd
            inverse_reduced = mod_inverse(a_reduced, m_reduced)
            single_solution = (inverse_reduced * b_reduced) % m_reduced
            solutions = [(single_solution + i * m_reduced) % m for i in range(gcd)]
            return solutions

# Сравнение: 3x ≡ 19 (mod 34)
a = 3
b = 19
m = 34

solution_1 = solve_linear_congruence(a, b, m)

print("Решение:", solution_1)
