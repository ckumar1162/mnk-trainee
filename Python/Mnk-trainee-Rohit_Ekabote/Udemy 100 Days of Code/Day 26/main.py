import random
# numbers = [1,2,3]
# new_numbers = [i+1 for i in numbers]
# print(new_numbers)
#
# name = "Rohit"
# name = [i for i in name]
# print(name)
#
# range_list = [i*2 for i in range(1, 5)]
# print(range_list)
#
# names = ['alex', 'beth', 'caroline', 'dave', 'elanor', 'freddie']
# short_name = [name for name in names if len(name) < 5]
# print(short_name)
# long_name = [name.upper() for name in names if len(name) > 5]
# print(long_name)
#
# student_score = {student:random.randint(1, 100) for student in names}
# print(student_score)
# passed_student = {student:score for (student, score) in student_score.items() if score >= 60}
# print(passed_student)
import pandas
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(value)

# for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    # print(row.student)
    # print(row.score)
    # if row.student == "Angela":
        # print(row)
        # print(row.score)

#{new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data.to_dict())

phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

word = input("enter the word: ").upper()
output = [phonetic_dict[letter] for letter in word]
print(output)
