import random

print("Welcome to the number guesser")

top_range = input("Enter a number ")

if top_range.isdigit():
    top_range = int(top_range)
    
if top_range <= 0:
    print("Please enter a number larger then 0 and try again ")
    exit()
    
    
random_number = random.randint(0, top_range)

while True:
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number: ")
        continue
    if user_guess == random_number:
        print("You got the number!")
        break
    elif user_guess > random_number:
        print("You are above the number. ")
    else:
        print("Below the number. ")
    
        