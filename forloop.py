import random

num = random.randint(1,10)

guess = int(input("can you guess the number what i am thinking"))

while num != guess:
    if guess > num:
        print("num is higher")
    else:
        print("num is lower")
    guess = int(input("guess again"))
else:
    print ("you won")