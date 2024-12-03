#caeser cipher
alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

user_input = input("Type 'encode' for encrpyt and 'decode' for decrypt\n")
msg = input("Type ur message\n")
shift = int(input("Type the shift number\n"))

# def encrpyt(og_text,shift_num):
#     cipher_caeser = ""
#     for i in og_text:
#         shift_position = alphabet.index(i) + shift_num
#         shift_position %=len(alphabet) 
#         cipher_caeser += alphabet[shift_position]
#     print(cipher_caeser)
# encrpyt(msg,shift)        

# def decrypt(og_text,shift_num):
#     decoded = ""
#     for i in og_text:
#         shift_position = alphabet.index(i) - shift_num
#         shift_position %=len(alphabet) 
#         decoded += alphabet[shift_position]
#     print(decoded)
# decrypt(msg,shift)    


def caeser(og_txt,shift_num,encode_or_decode):
    output =""
    if encode_or_decode == "decode":
            shift_num *= -1
    for i in og_txt:
        shift_position = alphabet.index(i) + shift_num
        shift_position %=len(alphabet) 
        output += alphabet[shift_position]
    print(output)
caeser(msg,shift,user_input)    













# alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def ceaser(orginal_text,shift,encode_or_decode):
#     output=""
#     if encode_or_decode == "decode":
#         shift *= -1
#     for i in orginal_text:
#         # TODO: What happens if user enters symbols or number or space?
#         if i not in alphabet:
#             output+=i
#         else:
#             shifted_position = alphabet.index(i) + shift
#             shifted_position %= len(alphabet)
#             output += alphabet[shifted_position]
#     print(f"Here is the {encode_or_decode}ed result: {output}")

# repeat=True
# while repeat:
#     direction=input('Type "encode" to encrypt, type "decode" to decrypt\n')
#     msg=input("Type your message:\n").lower()
#     shift_number=int(input("Type the shift number:\n"))
#     ceaser(msg, shift_number, direction)
#     try_again=input("Type 'yes' for go again.Otherwise type 'no'.\n").lower()

#     if try_again=='no':
#         repeat=False
#         print("GoodBye..")