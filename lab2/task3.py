class ModularExponentiation:
    def __init__(self, modulus):
        self.modulus = modulus

    def multiply_modulo(self, a, b):
        return (a * b) % self.modulus

    def add_modulo(self, a, b):
        return (a + b) % self.modulus

    def power(self, base, exponent):
        if exponent == 0:
            return 1
        elif exponent < 0:
            phi_m = self.calculate_phi(self.modulus)
            exponent = phi_m - 1

        result = 1
        while exponent > 0:
            if exponent % 2 == 1:
                result = self.multiply_modulo(result, base)
            base = self.multiply_modulo(base, base)
            exponent //= 2
        return result

    def calculate_phi(self, n):
        phi = n
        p = 2
        while p * p <= n:
            if n % p == 0:
                while n % p == 0:
                    n //= p
                phi -= phi // p
            p += 1
        if n > 1:
            phi -= phi // n
        return phi

# Пример использования:
mod_exp = ModularExponentiation(13)
print("3^4 mod 13 =", mod_exp.power(3, 4))
print("5^(-1) mod 13 =", mod_exp.power(5, -1))
