import random
import unittest

import mod_exp


class TestModExp(unittest.TestCase):
    def test_mod_exp(self):
        for _ in range(1000):
            a = random.randrange(pow(2, 1024))
            b = random.randrange(pow(2, 1024))
            c = random.randrange(pow(2, 1024))

            value = mod_exp.mod_exp(a, b, c)

            self.assertEqual(value, pow(a, b, c))
