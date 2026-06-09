import random
#that is double colored ball
# n = int(input('How many tickets do you want to generate? '))
# red_balls = [i for i in range(1, 34)]
# blue_balls = [i for i in range(1, 17)]

# for _ in range(n):
#     selected_balls = random.sample(red_balls, 6)
#     selected_balls.sort()

#     # \033[031m colors text red, \033[0m resets it
#     for ball in selected_balls:
#         print(f'\033[031m{ball:0>2d}\033[0m', end=' ')

#     blue_ball = random.choice(blue_balls)
#     print(f'\033[034m{blue_ball:0>2d}\033[0m') # Blue text


#powerball here

def one_ticket():
    whiteb_range = [i for i in range(1, 70)]
    pb_range = [i for i in range(1, 27)]
    wb = random.sample(whiteb_range, 5) 
    #.sample() is not a universal tool that works on everything. It is a highly specific tool that only exists inside the random module.
    wb.sort()
    pb = random.choice(pb_range)
    return wb, pb

n = int(input('How many tickets do you want to generate? '))
for _ in range(n):
    wb, pb = one_ticket()
    # 1. Format all white balls in a single line
    formatted_wb = " ".join([f"\033[0;37m{ball:0>2d}\033[0m" for ball in wb])
    
    # 2. Print the formatted white balls and the Powerball together
    print(f"{formatted_wb} \033[0;31m{pb:0>2d}\033[0m")