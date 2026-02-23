import random

minimum = 1
largest = 10
minlarg = random.randint(minimum, largest)

def test():
    choose = int(input('enter number 1-10: '))
    if choose > 10:
        print('no too high')
        return test()
    elif choose < 1:
        print('y would u go less than 1?')
