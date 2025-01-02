student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    print(key,value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    print(row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}


data=pandas.read_csv('nato_phonetic_alphabet.csv')
print(data)

phonetic={row.letter:row.code for (index,row) in data.iterrows()}
print(phonetic)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

words=input("Enter your word!").upper()
result=[phonetic[word] for word in words]
print(result)