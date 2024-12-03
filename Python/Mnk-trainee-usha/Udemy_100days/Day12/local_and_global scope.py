# num=1
# def add():
#     num2=2
#     print(num,num2)
# add()
#modifying global scope
enemy=6
def kill():
    global enemy
    
    enemy+=1
    print(f"kill {enemy} enemies")
kill()
print(f"kill {enemy} enemies")