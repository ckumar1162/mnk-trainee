import pandas

data=pandas.read_csv('nato_phonetic_alphabet.csv')

phonetic={row.letter:row.code for (index,row) in data.iterrows()}
print(phonetic)

def generate_phonetic():
    words=input("Enter your word!").upper()
    try:
        result=[phonetic[word] for word in words]
    except KeyError:
        print("sorry,only alphabets are required to enter ")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()