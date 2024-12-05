# alphabet_list = [chr(i) for i in range(97, 123)]
from operator import index


alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(orginal_text,shift,encode_or_decode):
    output=""
    if encode_or_decode == "decode":
        shift *= -1
    for i in orginal_text:
        # TODO: What happens if user enters symbols or number or space?
        if i not in alphabet:
            output+=i
        else:
            shifted_position = alphabet.index(i) + shift
            shifted_position %= len(alphabet)
            output += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}ed result: {output}")

repeat=True
while repeat:
    direction=input('Type "encode" to encrypt, type "decode" to decrypt\n')
    msg=input("Type your message:\n").lower()
    shift_number=int(input("Type the shift number:\n"))
    ceaser(msg, shift_number, direction)
    try_again=input("Type 'yes' for go again.Otherwise type 'no'.\n").lower()

    if try_again=='no':
        repeat=False
        print("GoodBye..")


# TODO 1: create a function for encrypt the message
# def encrpt(msg,shift_amount):
#     encrp_code=""
#     for i in msg:
#         shift_letter=alphabet.index(i)+shift_amount
#         # TODO 2: what happens if you try to shift z forwards by 9?
#         index=shift_letter % len(alphabet)
#
#         encrp_code+=alphabet[index]
#     print(f"Here is the encoded result: {encrp_code}")
#
#
# encrpt(msg,shift_number)
#
#
# def decrypt(orginal_text,shift_position):
#     enco=""
#     for i in orginal_text:
#         shifted_position=alphabet.index(i) - shift_position
#
#         shifted_position%=len(alphabet)
#
#         enco+=alphabet[shifted_position]
#     print(f"Decoded message : {enco}")
#
#
#
# decrypt(msg,shift_number)

