letters = [['x', 'w', 'z'], ['a', 'b', 'c'], ['p', 'y', 'q']]
#to remove one letter, use pop() or del:
letters[0].pop(1) # removes 'w'
del letters[1][0] # removes 'a'
print(letters) # [['x', 'z'], ['b', 'c'], ['p, 'y', 'q']]
print(len(letters)) # 3
