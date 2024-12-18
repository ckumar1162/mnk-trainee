class Dog:
    def __init__(self):
        self.behavior = "loyal"

    def bark(self):
        print("Woof, woof!")

class Labrador(Dog):
    def __init__(self):
        self.behavior = "friendly"

lab = Labrador()
lab.bark()
print(lab.behavior)

# original_list = ['Red', 'Green', 'Blue', 'White', 'Black']
# # ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
#
# list2 = []
#
# for i in original_list:
#     str1 = ""
#     for j in i:
#         str1 = j + str1
#     list2.append(str1)
#     # print(str1)
# print(list2)
