import os
import tkinter

import hash
from alice import Alice
from bob import Bob
from rsa import RSA
from signatures import Signatures

checksum = 0


# function that blind signs given data
def sign():
    text_value = text_message.get("1.0", 'end-1c')
    if os.path.isfile(text_value):
        with open(text_value, "rb") as file:
            message_data = file.read()
    else:
        message_data = text_value

    print("Message data is: {}".format(message_data))

    message_checksum = int(hash.gen_sha256(message_data), 16)

    blinded_message = alice.blind_message(message_checksum)
    blinded_signature = bob.sign(blinded_message)
    unblinded_signature = alice.unblind_signature(blinded_signature)

    text_signature.delete("1.0", "end")
    text_signature.insert("end", format(unblinded_signature, 'x'))

    print("Alice sends blinded message: {}".format(hex(blinded_message)))
    print("Bob sends blinded signature: {}".format(hex(blinded_signature)))
    print("Alice unblinds signature: {}".format(hex(unblinded_signature)))

    valid_signature = bob.sign(message_checksum)

    sig.valid_signature = valid_signature


def verify():
    sig.signature_from_textfield = text_signature.get("1.0", 'end-1c')

    sign_txt = int(sig.signature_from_textfield, 16)

    if sig.valid_signature == sign_txt:
        print("signature is valid!")
    else:
        print("signature is invalid!")


if __name__ == "__main__":
    rsa = RSA()
    alice = Alice(rsa.get_public_key())
    bob = Bob(rsa.get_private_key())

    sig = Signatures()

    message_checksum = 0
    valid_signature = 0

    window = tkinter.Tk()
    window.title("Ślepy podpis cyfrowy")

    # message for user
    message = tkinter.Message(window, text="Wpisz wiadomość lub ścieżkę do pliku, który chcesz podpisać:", width=600)
    message.pack()

    # text field to enter text or path to a file
    text_message = tkinter.Text(window, height=1, width=50)
    text_message.pack()

    # button to sign
    button = tkinter.Button(window, text="Podpisz wiadomość", command=sign)
    buttonVerify = tkinter.Button(window, text="Sprawdź", command=verify)
    button.pack()
    buttonVerify.pack()

    # blind signature label
    message_blind_signature = tkinter.Message(window, text="Podpis cyfrowy:", width=600)
    message_blind_signature.pack()

    # text field with calculated blind signature
    text_signature = tkinter.Text(window, height=12, width=50)
    text_signature.pack()

    window.mainloop()
