# #fibonacci sequence
# a, b = 0,1
# for _ in range(50):
#     a, b = b, a + b
#     print(a, end=' ')
# #narcissistic number
# for num in range(100, 1000):
#     low = num % 10
#     mid = num // 10 % 10
#     high = num // 100
#     if num == low ** 3 + mid ** 3 + high ** 3:
#         print(num)

#CRAPS
import random
money = 1000
while money > 0:
    print('Current money: ', money)
    ifcontinue = False
    while True: 
        debt = int(input('Please input your bet: '))
        if debt > money:
            print('You cannot bet more than you have!')
        else:            
            break
    first = (random.randint(1, 7)+random.randint(1, 7))
    print('The first throw is: ', first)
    count = 1
    if first in (7, 11):
        print('You win!')
        money += debt
    elif first in (2, 3, 12):
        print('You lose!')
        money -= debt
    else:
        while True:
            count += 1 
            continue_throw = (random.randint(1, 7)+random.randint(1, 7))
            print(f'In your {count} round, you got number: {continue_throw}')
            if continue_throw == 7:
                print('You lose!')
                money -= debt
                break
            elif continue_throw == first:
                print('You win!')
                money += debt
                break
    print('Current money: ', money)
    while True:
        print('Would you like to continue? (y/n):')
        choice = input()
    # why print('Would you like to continue? (y/n):',choice= input()) is not working? why the input() will show before the print message?
        if choice == 'n':
            print('Thanks for playing!')
            exit(0)
        elif choice != 'y':
            print('Invalid input! Please input y or n.')
        else: 
            break
if money <= 0:
    print('You are out of money! Game over!')        

