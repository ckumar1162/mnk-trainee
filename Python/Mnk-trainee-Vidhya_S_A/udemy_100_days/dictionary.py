# # dictionary
# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades ={}
# for key, value in student_scores.items():
#     if 91 <= value <= 100:
#         grade = "Outstanding"
#     elif 81 <= value <=90:
#         grade = "Expectation"
#     elif 71 <= value <=80 :
#         grade = "Acceptable"
#     else:
#         grade = "fail"
#     student_grades[key] = grade
# print(student_grades)




# #practice
# travel = {
#     "India" : ["Bangalore","Delhi","Mumbai"],
#     "Germany": ["Berlin","Stuttgart"],
# }

# # how to access delhi from the dictionary travel
# print(travel["India"][1])


# nested_list = [1,2,[3,4,5]]
# print(nested_list[2][1])


travel = {
    "India" : {
       "city": ["Bangalore","Delhi","Mumbai"]
        },
    "Germany": {
        "city1":["Berlin","Stuttgart"],
        "name" : ["Vidhya","padma"]
    }
}
print(travel["Germany"]["city1"][1])