
#TODO 1. Create a dictionary in this format:
import pandas as pd

dict1 = pd.read_csv(r"mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\NATO-alphabet-start\NATO-alphabet-start\nato_phonetic_alphabet.csv")
new_dict = {row.letter:row.code for (index,row) in dict1.iterrows()}
# print(new_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_nato_alphabet():
    str1 = input("enter a word:").upper()
    try:
        new_list = [new_dict[i] for i in str1]
    except KeyError:
        print('Sorry, only letters in the alphabet please') 
        generate_nato_alphabet()
    else:       
        print(new_list)
generate_nato_alphabet()