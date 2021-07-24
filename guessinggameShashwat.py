import random
print("Number guessing game")

name=input("What is your name?")

hi="Hello "
print(hi+name)

number=random.randint(1,9)
print("You have 5 turns")
print("Play Well!")
#print(number)

chances=0

print("Hint:If no hint you are far")
print("Guess a number between 1 and 9")

while chances<5:
    guess=int(input("Enter your guess: "))
    if guess==number:
        print("Congratulation You Win",name)
        break
    elif guess>5<number:
        print("Hint: your guess was too close; ",guess)
        #print("hi1")
    elif guess<5>number:
        print("Hint: your guess was too close; ",guess) 
        #print("hi2")
    
    chances+=1
if not chances < 5:
    print("you lose!!! the no is",number)