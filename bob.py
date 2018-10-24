from mod_exp import mod_exp


class Bob:
    def __init__(self, private_key):
        self.d = private_key[0]
        self.n = private_key[1]

    def sign(self, message):
        return mod_exp(message, self.d, self.n)
