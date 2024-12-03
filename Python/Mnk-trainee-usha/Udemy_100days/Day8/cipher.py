letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(plain_text,shift_key): #hello h=7
    cipher_text=""
    for i in plain_text:
        if i in letter:
            position=letter.index(i)
            new_position=(position+shift_key)%26 # %26 is to get rid of index out of range error
            cipher_text+=letter[new_position]
        else:
            cipher_text+=i
    print(f"Your encrypted message is:{cipher_text}")

def decryption(cipher_text,shift_key):    #khoor
    plain_text = ""
    for i in cipher_text:
        if i in letter:
            position = letter.index(i)
            new_position = (position - shift_key) % 26  # %26 is to get rid of index out of range error
            plain_text += letter[new_position]
        else:
            plain_text+=i
    print(f"Your encrypted message is:{plain_text}")

end=False
while not end:
    msg=input("Type 'encrypt' for encryption and 'decrypt' for decryption:\n" )
    text=input("Type your message:\n")
    shift=int(input("Enter the shift key:\n"))
    if msg == "encrypt":
        encryption(plain_text=text,shift_key=shift)
    elif msg == "decrypt":
        decryption(cipher_text=text,shift_key=shift)
    play_again=input("Type 'yes' to continue , type 'no' to exit.\n")
    if play_again == "no":
        end=True
        print("Goodbye")

