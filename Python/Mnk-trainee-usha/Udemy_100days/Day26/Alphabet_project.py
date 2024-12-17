import pandas
df=pandas.read_csv("nato_phonetic_alphabet.csv")
#to create a dictionary in the format
d={row.letter:row.code for (index,row) in df.iterrows()}
#print(d)
while True:
    word=input("Enter the word: ").upper()
    try:
        output=[d[i] for i in word]
    except KeyError:
        print("Sorry ,only alphabet please")
        continue
    else:
        print(output)
        break