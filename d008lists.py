# items1 = [35, 12, 99, 68, 55, 35, 87]
# items2 = ['Python', 'Java', 'Go', 'Kotlin']
# items3 = [100, 12.3, 'Python', True]
# print(type(items1))  # <class 'list'>
# print(type(items3))  # <class 'list'>

# #convert sequence to list
# items4 = list(range(1, 10))
# items5 = list('hello')
# print(items4)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(items5)  # ['h', 'e', 'l', 'l', 'o']

i6 = [1, 2, 3, 4, 5]
#slicing
print(i6[1:5])  # [2, 3, 4, 5]
i7 = i6*2 # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(i7[-1:-10:-3])  # [5, 2, 4]