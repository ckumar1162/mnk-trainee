class User:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.follower=0
        self.following=0
    def follow(self,user):
        user.following +=1
        self.follower +=1



user1=User(1,"Ramnath")
print(user1.id)
print(user1.name)

user2=User(2,"Lavanya")
print(user2.id)
print(user2.name)

# calling follow method
user2.follow(user1)

print(user1.follower)
print(user1.following)

print(user2.follower)
print(user2.following)

