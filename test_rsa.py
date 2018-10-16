import random
import unittest

from rsa import RSA


class TestRsa(unittest.TestCase):
    def test_rsa(self):
        for _ in range(100):
            rsa = RSA(256)

            message = random.randrange(pow(2, 255), pow(2, 256) - 1)

            e, n = rsa.get_public_key()
            encrypted_message = pow(message, e, n)

            d, n = rsa.get_private_key()
            decrypted_message = pow(encrypted_message, d, n)

            self.assertEqual(message, decrypted_message)
