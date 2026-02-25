
class Candle:
    def __init__(self, scent, color):
        self.scent = scent
        self.color = color

I1 = Candle('cotton candy', 'blue & pink marbled')
I2 = Candle('wood', 'brown')
I3 = Candle('lemon', 'yellow')

candleset = [I1, I2, I3]
for i in candleset:
    print(f'{i.scent} {i.color} candle')

p = True

while p == True:
    choice = input('Which candle do you want to buy? (1, 2, or 3) ')
    if choice == '1':
        print(f'You have chosen the {I1.scent} {I1.color} candle.')
        p = False
    elif choice == '2':
        print(f'You have chosen the {I2.scent} {I2.color} candle.')
        p = False
    elif choice == '3':
        print(f'You have chosen the {I3.scent} {I3.color} candle.')
        p = False
    else:
        print('Invalid choice. Please choose 1, 2, or 3.') 

    
