import math
import time

import prime


# extended Euclidean algorithm
def xgcd(b, a):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0


# modular multiplicative inverse algorithm
def mod_inv(b, n):
    g, x, _ = xgcd(b, n)
    if g == 1:
        return x % n


class RSA:
    def __init__(self, prime_length=1024, e=65537):
        start = time.time() * 1000

        p = prime.gen_prime(prime_length)
        print("p = {}".format(p))

        q = prime.gen_prime(prime_length)
        print("q = {}".format(q))

        self.n = p * q
        print("n = {}".format(self.n))

        r = (p - 1) * (q - 1)
        print("r = {}".format(r))

        self.e = e
        print("e = {}".format(e))

        e_inverse = mod_inv(e, r)
        print("e^-1 mod r = {}".format(e_inverse))

        self.d = e_inverse % r
        print("d = {}".format(self.d))

        end = time.time() * 1000
        time_diff = math.ceil(end - start)

        print("finished creating RSA keys, took {} ms".format(time_diff))

    def get_public_key(self):
        return self.e, self.n

    def get_private_key(self):
        return self.d, self.n
