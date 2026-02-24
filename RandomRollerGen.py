import random

minimum = 1
largest = 10
minlarg = random.randint(minimum, largest)

def test():
 while True:
    try: choose = int(input(f"Guess a number between {minimum} and {largest}: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if choose < minimum or choose > largest:
        print(f"Please enter a number between {minimum} and {largest}.")
        continue
    else: break
 print(f'you choose {choose}, the number is {minlarg}')

test()

