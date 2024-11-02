import random
print("""Welcome to the Coin Guessing Game !
Choose a method to toss the coin:
1.Using random.random()
2.Using random.randint()""")
chois = input("Enter your choice (1 or 2): ")
#chois random and randint
if chois == '1':
    random_number = random.random()
    if random_number >= 0.5:
        computer_result = "Heads"
    else:
        computer_result = "Tails"
elif chois == '2':
    randint_number = random.randint(0,1)
    if randint_number == 0:
        computer_result = "Heads"
    else:
        computer_result = "Tails"
else:
    print(f"sorry , please 1 or 2 no {chois}")
#computer 
user_choice = input("Enter your Guess (Heads or Tails): ")
if user_choice.lower() == computer_result.lower():
    print("YOU WON!")
else:
    print("sorry , YOU LOST!")


print(f"THE computer's coin toss result was : {computer_result}")