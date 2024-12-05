#higher lower project
import random
data = [
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 600,
        "description": "Football player",
        "country": "Portugal",
    },
    {
        "name": "Kylie Jenner",
        "follower_count": 380,
        "description": "Model and businesswoman",
        "country": "United States",
    },
    {
        "name": "Lionel Messi",
        "follower_count": 480,
        "description": "Football player",
        "country": "Argentina",
    },
    {
        "name": "Selena Gomez",
        "follower_count": 420,
        "description": "Singer and actress",
        "country": "United States",
    },
    {
        "name": "Dwayne Johnson",
        "follower_count": 360,
        "description": "Actor and former wrestler",
        "country": "United States",
    },
    {
        "name": "Taylor Swift",
        "follower_count": 370,
        "description": "Singer-songwriter",
        "country": "United States",
    },
    {
        "name": "Kim Kardashian",
        "follower_count": 350,
        "description": "Reality TV star and businesswoman",
        "country": "United States",
    },
    {
        "name": "Ariana Grande",
        "follower_count": 380,
        "description": "Singer and actress",
        "country": "United States",
    },
    {
        "name": "Neymar Jr.",
        "follower_count": 240,
        "description": "Football player",
        "country": "Brazil",
    },
    {
        "name": "Virat Kohli",
        "follower_count": 260,
        "description": "Cricketer",
        "country": "India",
    },
    {
        "name": "Elon Musk",
        "follower_count": 220,
        "description": "Entrepreneur",
        "country": "United States",
    },
    {
        "name": "Billie Eilish",
        "follower_count": 110,
        "description": "Singer-songwriter",
        "country": "United States",
    },
    {
        "name": "Shakira",
        "follower_count": 140,
        "description": "Singer",
        "country": "Colombia",
    },
    {
        "name": "Rihanna",
        "follower_count": 250,
        "description": "Singer and businesswoman",
        "country": "Barbados",
    },
    {
        "name": "Zendaya",
        "follower_count": 180,
        "description": "Actress and singer",
        "country": "United States",
    },
]

count =0
#compare option A and option B with user choice
def compare(choice,a,b):
    if a > b:
        if choice == "A":
            return True
        else :
            return False 

should_continue = True
while should_continue:
    option_A = random.choice(data)
    option_B = random.choice(data)
    if option_A == option_B:
        option_B = random.choice(data)

        
    print(f"Compare A : {option_A['name']},{option_A['description']}, from {option_A['country']}")
    print("VS")
    print(f"Against B : {option_B['name']},{option_B['description']}, from {option_B['country']}")

    user_choice = input("Who has more followers:Type 'A'or 'B':").upper()
    #compare 'A' and 'B'
    
    compare_A = option_A["follower_count"] 
    compare_B = option_B["follower_count"]
    check = compare(user_choice,compare_A,compare_B)

    if check:
        count +=1
        print(f"You are right,and your score is {count}")
    else:
        print(f"Oh oh ! you are wrong ,final score :{count}")
        should_continue = False
    