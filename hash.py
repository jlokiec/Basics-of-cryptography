import hashlib


def gen_sha256(data):
    generator = hashlib.sha256()

    if type(data) is str:
        generator.update(data.encode())
    elif type(data) is bytes:
        generator.update(data)

    return generator.hexdigest()
