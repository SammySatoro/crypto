def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def calculate_prime_factors(N):
    prime_factors = []
    if N % 2 == 0:
        prime_factors.append(2)
    while N % 2 == 0:
        N = N // 2
        if N == 1:
            return prime_factors
    for factor in range(3, N + 1, 2):
        if N % factor == 0:
            prime_factors.append(factor)
            while N % factor == 0:
                N = N // factor
                if N == 1:
                    return prime_factors

def primitive_roots(p):
    if is_prime(p):
        p1 = p - 1
        roots = []
        prime_factors = calculate_prime_factors(p1)
        print(f"p-1 = {p1}")
        fi = f"fi({p1}) = {p1}*{'*'.join([f'(1 - 1/{i})' for i in prime_factors])}"
        fi_res = fi[(fi.find('=') + 2):]
        print(f"{fi} = {int(eval(fi_res))}")
        pows = ((p1) // prime_factors[0], (p1) // prime_factors[1])
        print("Проверяем числа от 2 до", p - 1, "на примитивность:")
        for g in range(2, p):
            temp = [pow(g, pows[0], p), pow(g, pows[1], p)]
            is_primitive = all(i != 1 for i in temp)
            if is_primitive:
                print(f"Число {g} является примитивным корнем: {g}^{pows[0]} mod {p} = {temp[0]}, {g}^{pows[1]} mod {p} = {temp[1]}")
                roots.append(g)
            else:
                print(f"Число {g} не является примитивным корнем: {g}^{pows[0]} mod {p} = {temp[0]}, {g}^{pows[1]} mod {p} = {temp[1]}")
        return roots
    else:
        return "Входное число не является простым."

p = 31  # Пример простого модуля
roots = primitive_roots(p)
print("Примитивные корни по модулю", p, ":", roots)