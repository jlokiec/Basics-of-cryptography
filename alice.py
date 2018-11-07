import math
import random

from mod_exp import mod_exp
from rsa import modular_inverse


class Alice:
    def __init__(self, public_key):
        self.e = public_key[0]
        self.n = public_key[1]
        self.r = self._get_random_factor()
        self.unblinded_signature = -1

    def blind_message(self, message):
        return (message * mod_exp(self.r, self.e, self.n)) % self.n

    def unblind_signature(self, blind_signature):
        r_modular_inverse = self._get_random_factor_modular_inverse()
        self.unblinded_signature = (blind_signature * r_modular_inverse) % self.n
        return self.unblinded_signature

    def _get_random_factor(self):
        random_factor = random.randrange(pow(2, 32))
        while not math.gcd(self.n, random_factor) == 1:
            random_factor = random.randrange(pow(2, 32))

        return random_factor

    def _get_random_factor_modular_inverse(self):
        return modular_inverse(self.r, self.n)
