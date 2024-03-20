def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise Exception('Обратного элемента не существует')
    else:
        return x % m

def chinese_remainder_theorem(congruences):
    M = 1
    for _, m in congruences:
        M *= m

    result = 0
    for a, m in congruences:
        M_i = M // m
        inv = mod_inverse(M_i, m)
        result += a * M_i * inv

    return result % M

# Пример использования:
congruences = [(8, 6), (13, 35), (4, 11)]
solution = chinese_remainder_theorem(congruences)
print("Решение системы сравнений:", solution)
