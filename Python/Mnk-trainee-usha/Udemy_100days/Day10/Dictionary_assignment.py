# dictionary assignment
student_marks = {
    "aishu" :98,
    "usha" :80,
    "pinky":85,
    "raju" :60,
    "golla" :40,
    "you" :34
}
student_grade={}
for key in student_marks:#aishu
    marks= student_marks[key]#98
    if marks>90:
        student_grade[key]="A+"
    elif marks>80:
        student_grade[key]="A"
    elif marks>70:
        student_grade[key]="B+"
    elif marks>60:
        student_grade[key]="B"
    elif marks>50:
        student_grade[key]="C"
    elif marks>40:
        student_grade[key]="D"
    elif marks<40:
        student_grade[key]="Fail"
print(student_grade)