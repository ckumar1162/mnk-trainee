alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r']

def caesar(original_text,shift_amount,encode_or_decode):
    output_text=" "
    if encode_or_decode=="decode":
        shift_amount*= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text+=letter
        else:
            
            shifted_position=alphabet.index(letter)+shift_amount
            shifted_position %=len(alphabet)# so that it wont cross the limit 
            output_text+=alphabet[shifted_position]
    print(f"here is the {encode_or_decode}result:{output_text}")

should_continue=True

while should_continue:
    direction=input("type 'encode' to encrypt,type 'decode', to decrypt:\n").lower()
    text=input("type your message:\n").lower()
    shift=int(input("type the shift number:\n"))

    caesar(original_text=text,shift_amount=shift,encode_or_decode=direction)
    restart=input("type 'yes',if you want to go again.otherwise,type'no'.\n").lower()
    if restart=='no':
        should_continue==False
        print("goodbye")
