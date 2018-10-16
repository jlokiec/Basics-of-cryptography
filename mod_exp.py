# right-to-left binary method of modular exponentiation
def mod_exp(x, y, z):
    result = 1
    while y:
        if y & 1:
            result = result * x % z

        y >>= 1
        x = x * x % z

    return result
