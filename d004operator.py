# while True:
#     try:
#         f = float(input("Enter Fahrenheit: "))
#         # If the line above works, we break the loop
#         break 
#     except ValueError:
#         # If float() fails, it jumps here instead of crashing
#         print(" Warning: Please enter a valid number (e.g., 98.6).")

# c = (f - 32) * 5/9
# print(f"Celsius: {c:.2f}")
# print("temp conversion done, let's move on to assignment operators")

a=[1,2,3]
b=a
b.pop(1)
print(a) # a is also changed because b is just a reference to the same list
a=[1,2,3]
print(b) # b still references the old list, which is now [1,3]
