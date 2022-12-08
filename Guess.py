import random
c=random.randint(1,25)
for i in range (5):
    print(f'{5-i} chances left: ')
    u=int(input("Guess a number between 1 to 25: "))
    if u==c:
        print(f"Great Guess! You won in {i} guesses!")
        break
    elif u>c:
        print("The number is smaller than your guess...")
    elif u<c:
        print("The number is greater than your guess...")
else:
    print(f"The number is: {c}")
