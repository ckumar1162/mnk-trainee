# to add data to dictionary
student_data =[
    {
    "Name":"Usha",
    "Age": 22,
    "Course": "python"
    },
    {
      "Name":"Mnk",
      "Age": 25,
      "Course": "React",
    }
]

def add_student(name,age,course):
    new_student={}
    new_student["Name"]=name
    new_student["Age"]=age
    new_student["Course"]=course
    student_data.append(new_student)
add_student("Ram",30,"C++")
print(student_data)