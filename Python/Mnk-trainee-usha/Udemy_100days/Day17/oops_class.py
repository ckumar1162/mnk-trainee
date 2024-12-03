# class User:
#     pass
# print("hi")
# def function():
#     pass
# print("hello")# pass will not give an error
# class User:
#     pass
# user1=User()
# user1.id="001"
# user1.username="usha"
# print(user1.id)
#
# user2=User()
# user2.id="002"
# user2.username="pinky"
# print(user2.username)
from idlelib.configdialog import changes


#using a constructor
# class User:
#     def __init__(self,user_id,username):
#         self.id=user_id
#         self.name=username
#         #print(self.id,self.name)
# user1=User("001","usha")
# print(user1.id)

#adding method to class
class Car:
    def __init__(self,seats):
        self.seat=seats
        print(f"There are {seats} in the car ")
    def change_seat(self,seats):
        self.seatss=seats
        print(f"There are {seats} in tha car now")
car1=Car(5)
car1.change_seat(3)