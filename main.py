import os
import sys

import hash
from alice import Alice
from bob import Bob
from rsa import RSA

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if os.path.isfile(sys.argv[1]):
            with open(sys.argv[1], "rb") as file:
                message_data = file.read()
        else:
            message_data = sys.argv[1]

        message_checksum = int(hash.gen_sha256(message_data), 16)

        rsa = RSA(1024)
        alice = Alice(rsa.get_public_key())
        bob = Bob(rsa.get_private_key())

        blinded_message = alice.blind_message(message_checksum)
        blinded_signature = bob.sign(blinded_message)
        unblinded_signature = alice.unblind_signature(blinded_signature)

        print("Alice sends blinded message: {}".format(hex(blinded_message)))
        print("Bob sends blinded signature: {}".format(hex(blinded_signature)))
        print("Alice unblinds signature: {}".format(hex(unblinded_signature)))

        valid_signature = bob.sign(message_checksum)

        if valid_signature == unblinded_signature:
            print("signature is valid!")
        else:
            print("signature is invalid")

    else:
        print("specify message or file path")
