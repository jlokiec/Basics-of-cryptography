import math
import random
from mod_exp import mod_exp


def extended_gcd(b, a):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0


def modular_inverse(b, n):
    g, x, _ = extended_gcd(b, n)
    if g == 1:
        return x % n


class Alice:
    def __init__(self, public_key):
        self.e = public_key[0]
        self.n = public_key[1]
        self.r = self._get_random_factor()

    def blind_message(self, message):
        return (message * mod_exp(self.r, self.e, self.n)) % self.n

    def unblind_signature(self, blind_signature):
        r_modular_inverse = self._get_random_factor_modular_inverse()
        return (blind_signature * r_modular_inverse) % self.n

    def _get_random_factor(self):
        random_factor = random.randrange(pow(2, 32))
        while not math.gcd(self.n, random_factor) == 1:
            random_factor = random.randrange(pow(2, 32))

        return random_factor

    def _get_random_factor_modular_inverse(self):
        return modular_inverse(self.r, self.n)
