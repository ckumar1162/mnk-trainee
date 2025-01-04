import pandas as pd


data = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter : row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def phonetic_word():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]

    except KeyError:
        print("pls enter alphabet")
        phonetic_word()
    else:
        print(output_list)
phonetic_word()

